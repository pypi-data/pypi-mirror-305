import asyncio
from typing import List, Dict, Any, AsyncGenerator
from botrun_flow_lang.models.nodes.base_node import BaseNode, NodeType
from botrun_flow_lang.models.workflow import Workflow, WorkflowItem
from botrun_flow_lang.models.nodes.event import (
    NodeEvent,
    NodeRunStartedEvent,
    NodeRunCompletedEvent,
    NodeRunStreamEvent,
    WorkflowRunStartedEvent,
    WorkflowRunCompletedEvent,
    WorkflowRunFailedEvent,
)


class WorkflowEngine:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow
        self.variable_pool: Dict[str, Dict[str, Any]] = {}

    async def execute(
        self, initial_inputs: Dict[str, Any]
    ) -> AsyncGenerator[NodeEvent, None]:
        yield WorkflowRunStartedEvent()
        self.variable_pool.update(initial_inputs)

        try:
            async for event in self._execute_items(self.workflow.items):
                yield event

            yield WorkflowRunCompletedEvent(outputs=self.variable_pool)
        except Exception as e:
            yield WorkflowRunFailedEvent(error=str(e))

    async def _execute_items(
        self, items: List[WorkflowItem]
    ) -> AsyncGenerator[NodeEvent, None]:
        for item in items:
            if item.node:
                yield NodeRunStartedEvent(
                    node_id=item.node.data.id,
                    node_title=item.node.data.title,
                    node_type=item.node.data.type.value,
                    is_print=item.node.data.print_start,
                )

                if item.node.data.type == NodeType.ITERATION:
                    async for event in self._execute_iteration(item.node, item.items):
                        yield event
                else:
                    async for event in item.node.run(self.variable_pool):
                        if isinstance(event, NodeRunStreamEvent):
                            yield event
                        elif isinstance(event, NodeRunCompletedEvent):
                            item.node.update_variable_pool(
                                self.variable_pool, event.outputs
                            )
                            yield event
                        else:
                            yield event

    async def _execute_iteration(
        self, iteration_node: BaseNode, sub_items: List[WorkflowItem]
    ) -> AsyncGenerator[NodeEvent, None]:
        input_list = iteration_node.get_variable(
            self.variable_pool,
            iteration_node.data.input_selector.node_id,
            iteration_node.data.input_selector.variable_name,
        )

        if not isinstance(input_list, list):
            raise ValueError(
                f"Input for IterationNode must be a list, got {type(input_list)}"
            )

        outputs = []
        is_async = iteration_node.data.is_async

        async def process_item(index, item):
            self.variable_pool[iteration_node.data.id] = {"item": item, "index": index}

            async for event in self._execute_items(sub_items):
                yield event

            output = iteration_node.get_variable(
                self.variable_pool,
                iteration_node.data.output_selector.node_id,
                iteration_node.data.output_selector.variable_name,
            )
            outputs.append(output)

            yield NodeRunStreamEvent(
                node_id=iteration_node.data.id,
                node_title=iteration_node.data.title,
                node_type=iteration_node.data.type.value,
                chunk=f"Iteration {index + 1}/{len(input_list)} completed",
                is_print=iteration_node.data.print_stream,
            )

        if is_async:
            tasks = [
                self._process_item_wrapper(process_item(index, item))
                for index, item in enumerate(input_list)
            ]
            completed_tasks = await asyncio.gather(*tasks)
            for events in completed_tasks:
                for event in events:
                    yield event
        else:
            for index, item in enumerate(input_list):
                async for event in process_item(index, item):
                    yield event

        iteration_node.update_variable_pool(self.variable_pool, {"output": outputs})
        yield NodeRunCompletedEvent(
            node_id=iteration_node.data.id,
            node_title=iteration_node.data.title,
            node_type=iteration_node.data.type.value,
            outputs={"output": outputs},
            is_print=iteration_node.data.print_complete,
        )

    async def _process_item_wrapper(self, generator):
        events = []
        async for event in generator:
            events.append(event)
        return events


async def run_workflow(
    workflow: Workflow, initial_inputs: Dict[str, Any]
) -> AsyncGenerator[NodeEvent, None]:
    engine = WorkflowEngine(workflow)
    async for event in engine.execute(initial_inputs):
        yield event

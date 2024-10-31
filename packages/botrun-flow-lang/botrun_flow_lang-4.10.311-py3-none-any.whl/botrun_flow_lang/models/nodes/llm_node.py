from pydantic import BaseModel, Field
from typing import List, Dict, Any, AsyncGenerator
from botrun_flow_lang.models.nodes.base_node import BaseNode, BaseNodeData, NodeType
import litellm
from botrun_flow_lang.models.nodes.event import (
    NodeEvent,
    NodeRunStreamEvent,
    NodeRunCompletedEvent,
)

import os
from dotenv import load_dotenv

load_dotenv()


class LLMModelConfig(BaseModel):
    completion_params: Dict[str, Any] = Field(default_factory=dict)
    name: str


class LLMNodeData(BaseNodeData):
    type: NodeType = NodeType.LLM
    model: LLMModelConfig
    prompt_template: List[Dict[str, str]]
    context: Dict[str, Any] = Field(default_factory=dict)
    vision: Dict[str, bool] = Field(default_factory=dict)
    print_stream: bool = True


class LLMNode(BaseNode):
    data: LLMNodeData

    async def run(
        self, variable_pool: Dict[str, Dict[str, Any]]
    ) -> AsyncGenerator[NodeEvent, None]:
        messages = self.prepare_messages(variable_pool)

        stream = await litellm.acompletion(
            model=self.data.model.name,
            messages=messages,
            stream=True,
            api_key=get_api_key(self.data.model.name),
            **self.data.model.completion_params
        )

        full_response = ""
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                yield NodeRunStreamEvent(
                    node_id=self.data.id,
                    node_title=self.data.title,
                    node_type=self.data.type.value,
                    chunk=content,
                    is_print=self.data.print_stream,
                )

        yield NodeRunCompletedEvent(
            node_id=self.data.id,
            node_title=self.data.title,
            node_type=self.data.type.value,
            outputs={"llm_output": full_response},
            complete_output=self.data.complete_output,
            is_print=self.data.print_complete,
        )

    def prepare_messages(self, variable_pool):
        messages = []
        for message in self.data.prompt_template:
            content = self.replace_variables(message["content"], variable_pool)
            messages.append({"role": message["role"], "content": content})
        return messages


def get_api_key(model_name: str) -> str:
    if model_name.find("TAIDE-") != -1:
        return os.getenv("TAIDE_API_KEY", "")
    elif model_name.startswith("anthropic"):
        return os.getenv("ANTHROPIC_API_KEY", "")
    elif model_name.startswith("openai"):
        return os.getenv("OPENAI_API_KEY", "")
    elif model_name.startswith("gemini"):
        return os.getenv("GEMINI_API_KEY", "")
    elif model_name.startswith("together_ai"):
        return os.getenv("TOGETHERAI_API_KEY", "")
    elif model_name.startswith("deepinfra"):
        return os.getenv("DEEPINFRA_API_KEY", "")
    else:
        return ""

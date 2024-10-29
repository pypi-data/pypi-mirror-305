from typing import Any, Dict, List, Optional

import numpy as np
from tecton import (
    Attribute,
    FeatureService,
    FeatureView,
    RealtimeFeatureView,
    realtime_feature_view,
)
from tecton.types import String

from ..deco import _get_from_metastore, _get_source_names
from ..utils._internal import (
    _REQUEST,
    entity_to_tool_schema,
    fields_to_tool_schema,
    set_serialization,
)


class AgentService:
    """
    AgentService is a class that helps to create a collection of feature services
    from a list of tools, prompts, and knowledge bases.

    Args:

        name: The name of the agent service
        prompts: A list of prompts
        tools: A list of tools, features views can be used as tools directly
        knowledge: A list of knowledge bases
        **feature_service_kwargs: The keyword arguments for the feature services

    Example:

        Let's build a chatbot helping a student to shop for items.

        ```python
        from tecton_gen_ai.testing import make_local_source, make_local_batch_feature_view, set_dev_mode
        from tecton_gen_ai.testing.utils import make_local_vector_db_config

        set_dev_mode()  # Set the dev mode to avoid tecton login

        student = make_local_batch_feature_view(
            "student",
            {"student_id": 1, "name": "Jim", "teacher": "Mr. Smith", "preference": "fruit"},
            ["student_id"],
            description="Student information including name, teacher and shopping preference",
        )

        df = [
            {"zip":"98005", "item_id":1, "description":"pencil"},
            {"zip":"98005", "item_id":2, "description":"car"},
            {"zip":"98005", "item_id":3, "description":"paper"},
            {"zip":"10065", "item_id":4, "description":"boat"},
            {"zip":"10065", "item_id":5, "description":"cheese"},
            {"zip":"10065", "item_id":6, "description":"apple"},
        ]

        src = make_local_source(
            "for_sale",
            df,
            description="Items information",  # required for source_as_knowledge
        )
        vdb_conf = make_local_vector_db_config()

        # Create a knowledge base from the source
        from tecton_gen_ai.api import prompt, source_as_knowledge

        @prompt(sources=[student])
        def sys_prompt(student) -> str:
            return "You are serving a 4 years old child "+student["name"]

        knowledge = source_as_knowledge(
            src,
            vector_db_config=vdb_conf,
            vectorize_column="description",
            filter = [("zip", str, "the zip code of the item for sale")]
        )

        # Serve the knowledge base
        from tecton_gen_ai.api import AgentService

        service = AgentService(
            "app",
            prompts=[sys_prompt],
            tools=[student],  # student is a feature view but can be used as a tool directly
            knowledge=[knowledge],
        )

        # Test locally
        from langchain_openai import ChatOpenAI

        openai = ChatOpenAI(model = "gpt-4o", temperature=0)

        from tecton_gen_ai.api import AgentClient

        client = AgentClient.from_local(service)
        client.default_llm = openai
        with client.set_context({"zip":"98005", "student_id":1}):
            print(client.invoke_agent("Suggest something for me to buy"))
        with client.set_context({"zip":"10065", "student_id":1}):
            print(client.invoke_agent("Suggest something for me to buy"))
        ```
    """

    def __init__(
        self,
        name: str,
        prompts: Optional[List[Any]] = None,
        tools: Optional[List[Any]] = None,
        knowledge: Optional[List[Any]] = None,
        **feature_service_kwargs: Any,
    ):
        self.name = name
        self.tools: List[Any] = []
        self.prompts: List[Any] = []
        self.knowledge_bfvs: List[FeatureView] = []
        self.metastore: Dict[str, Any] = {}
        if prompts:
            for prompt in prompts:
                self._add_prompt(prompt)
        if tools:
            for tool in tools:
                if isinstance(tool, FeatureView):
                    self._add_fv_tool(fv_as_tool(tool, queryable=False))
                elif isinstance(tool, FeatureViewTool):
                    self._add_fv_tool(tool)
                else:
                    self._add_tool(tool)
        if knowledge:
            for k in knowledge:
                self._add_knowledge(k)
        self.online_fvs: List[RealtimeFeatureView] = [
            *self.tools,
            *self.prompts,
            self._make_metastore(),
        ]
        self._run(name, **feature_service_kwargs)

    def _add_tool(self, func: Any) -> None:
        meta = dict(_get_from_metastore(func))
        if meta.get("type") != "tool":
            raise ValueError(f"Function {func} is not a tool")
        name = meta.pop("name")
        self.tools.append(meta.pop("fv"))
        self.metastore[name] = meta

    def _add_fv_tool(self, fvt: "FeatureViewTool") -> None:
        self.metastore[fvt.fv.name] = fvt.make_metadata()
        self.tools.append(fvt.make_rtfv())

    def _add_prompt(self, func: Any) -> None:
        meta = dict(_get_from_metastore(func))
        if meta.get("type") != "prompt":
            raise ValueError(f"Function {func} is not a prompt")
        name = meta.pop("name")
        self.prompts.append(meta.pop("fv"))
        self.metastore[name] = meta

    def _add_knowledge(self, funcs: Any) -> None:
        self.knowledge_bfvs.append(funcs[0])
        self._add_tool(funcs[1])

    def _make_metastore(self) -> FeatureView:
        _metastore = self.metastore

        with set_serialization():

            @realtime_feature_view(
                name="metastore",
                sources=[_REQUEST],
                mode="python",
                features=[Attribute("output", String)],
            )
            def metastore(request_context) -> str:
                import json

                if "metastore" != request_context["name"]:
                    return {"output": "{}"}
                return {"output": json.dumps({"result": _metastore})}

            return metastore

    def _run(self, name: str, **kwargs) -> List[FeatureService]:
        fs = [
            FeatureService(name=name + "_" + tool.name, **kwargs, features=[tool])
            for tool in self.online_fvs
        ]
        for fv in self.knowledge_bfvs:
            fs.append(
                FeatureService(
                    name=name + "_" + fv.name,
                    **kwargs,
                    features=[fv],
                    online_serving_enabled=False,
                )
            )
        return fs


def fv_as_tool(
    fv: FeatureView, queryable: bool, description: Optional[str] = None
) -> "FeatureViewTool":
    """Convert a feature view to a tool

    Args:

        fv: The feature view
        queryable: Whether the tool is queryable using its entity ids
        description: The description of the tool, default to None. If provided,
            it will be used as the description of the tool

    Returns:

        A FeatureViewTool object
    """
    return FeatureViewTool(fv, queryable, description=description)


class FeatureViewTool:
    def __init__(
        self, fv: FeatureView, queryable: bool, description: Optional[str] = None
    ):
        if not isinstance(fv, FeatureView):
            raise ValueError(f"Expected FeatureView, got {type(fv)}")
        if not hasattr(fv, "entities") or len(fv.entities) != 1:
            raise ValueError(f"FeatureView {fv} must have exactly one entity")
        self.description = description or fv.description
        if not self.description:
            raise ValueError(
                f"FeatureView {fv} must have a description or you "
                "should provide the description from `fv_as_tool`"
            )

        self.fv = fv
        self.queryable = queryable
        self.tool_name = "fv_tool_" + fv.name

    def make_metadata(self):
        fv = self.fv
        description = self.description
        fv_schema = fields_to_tool_schema(fv.transformation_schema())
        # notice transformation_schema doesn't consider aggregation, so this is not the final schema
        # gettting entity schema from it is fine
        schema = entity_to_tool_schema(fv.entities[0], fv_schema)
        return {
            "name": self.tool_name,
            "type": "tool",
            "subtype": "fv",
            "schema": schema,
            "queryable": self.queryable,
            "description": description,
            "source_names": _get_source_names([fv]),
        }

    def make_rtfv(self) -> RealtimeFeatureView:
        fv = self.fv
        tool_name = self.tool_name
        with set_serialization():

            @realtime_feature_view(
                name=tool_name,
                sources=[_REQUEST, fv],
                mode="python",
                features=[Attribute("output", String)],
            )
            def fv_tool(request_context, _fv) -> str:
                import json

                if tool_name != request_context["name"]:
                    return {"output": "{}"}
                res = _transform_group_result(_fv)
                return {"output": json.dumps({"result": res})}

            return fv_tool


def _transform_group_result(fv: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Transform the group result to a list of dictionaries

    Args:

        fv: a dict of single value or arrays

    Returns:

        List[Dict[str, Any]]: a list of dictionaries
    """
    cols: List[List[Any]] = [
        v.tolist() for v in fv.values() if isinstance(v, np.ndarray)
    ]
    if len(cols) == 0:
        return fv
    elif len(cols) < len(fv):
        raise ValueError("All columns must be numpy arrays or none")
    blobs = []
    keys = list(fv.keys())
    step = len(fv) // 2
    for i in range(step):
        key_name = keys[i].rsplit("_keys_", 1)[0]
        val_name = keys[i + step]
        blob = [{key_name: x, val_name: y} for x, y in zip(cols[i], cols[i + step])]
        blobs.extend(blob)
    return blobs

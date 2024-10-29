import pandas as pd
from pytest import fixture

from tecton_gen_ai.utils.tecton_utils import make_request_source
from tecton_gen_ai.api import (
    AgentClient,
    AgentService,
    prompt,
    tool,
)
from tecton_gen_ai.testing import make_local_batch_feature_view


@fixture
def mock_data():
    return pd.DataFrame(
        [
            {
                "user_id": "user1",
                "name": "Jim",
                "age": 30,
                "food_preference": "American",
            },
            {
                "user_id": "user2",
                "name": "John",
                "age": 40,
                "food_preference": "Italian",
            },
            {
                "user_id": "user3",
                "name": "Jane",
                "age": 50,
                "food_preference": "Chinese",
            },
        ]
    )


@fixture
def mock_agent_service(tecton_unit_test, mock_data, mock_knowledge):
    user_info = make_local_batch_feature_view(
        "user_info", mock_data, entity_keys=["user_id"], description="User info"
    )

    @prompt(sources=[user_info])
    def sys_prompt(location: str, user_info):
        name = user_info["name"]
        return f"You are serving {name} in {location}"

    request = make_request_source(location=str)

    @prompt(sources=[request, user_info])
    def sys_prompt_request_source(request, user_info):
        name = user_info["name"]
        location = request["location"]
        return f"You are serving {name} in {location}"

    @tool
    def get_tecton_employee_count() -> int:
        """
        Returns the number of employees in Tecton
        """
        return 110

    return AgentService(
        name="test",
        prompts=[sys_prompt, sys_prompt_request_source],
        tools=[user_info, get_tecton_employee_count],
        knowledge=[mock_knowledge],
    )


def test_agent(mock_agent_service):
    client = AgentClient.from_local(mock_agent_service)
    assert (
        client.invoke_prompt("sys_prompt", dict(user_id="user3", location="Chicago"))
        == "You are serving Jane in Chicago"
    )
    assert (
        client.invoke_prompt(
            "sys_prompt_request_source", dict(user_id="user3", location="Chicago")
        )
        == "You are serving Jane in Chicago"
    )
    assert client.invoke_tool("user_info", dict(user_id="user1")) == {
        "name": "Jim",
        "age": 30,
        "food_preference": "American",
    }
    assert client.invoke_tool("get_tecton_employee_count") == 110

    assert client.search("knowledge", query="food", filter={"zip": 98010}) == []
    assert (
        len(client.search("knowledge", query="food", top_k=5, filter={"zip": 98005}))
        == 3
    )
    assert len(client.search("knowledge", query="food", top_k=5)) == 5

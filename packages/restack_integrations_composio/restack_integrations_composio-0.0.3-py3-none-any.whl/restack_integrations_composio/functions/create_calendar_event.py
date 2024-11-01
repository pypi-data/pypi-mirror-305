from restack_integrations_openai import openai_chat_completion_base, OpenAIChatInput
from composio_openai import Action
from pydantic import BaseModel

from typing import Optional

from ..utils.toolsets import openai_toolset
from .initiate_connection import initiate_connection, InitiateConnectionInput


class CreateCalendarEventInput(BaseModel):
    calendar_instruction: str 
    entity_id: str
    composio_api_key: Optional[str] = None
    wait_until_active: Optional[int] = None

APP_NAME = "googlecalendar"

async def create_calendar_event(
    input: CreateCalendarEventInput
):
    composio_openai_toolset = openai_toolset(entity_id=input.entity_id)

    initiate_connection_response = initiate_connection(
        input=InitiateConnectionInput(
            entity_id=input.entity_id,
            app_name=APP_NAME,
            composio_api_key=input.composio_api_key,
            wait_until_active=input.wait_until_active
        )
    )

    if (initiate_connection_response["authenticated"] == "no"):
        return initiate_connection_response

    tools = composio_openai_toolset.get_tools(actions=[Action.GOOGLECALENDAR_CREATE_EVENT])

    response = openai_chat_completion_base(
        OpenAIChatInput(
            user_content=input.calendar_instruction,
            tools=tools,
        )
    )

    composio_openai_toolset.handle_tool_calls(response.result)

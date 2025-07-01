from app.facades.message_facade import get_message_facade, MessageFacade
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.messages_api.message import Message
from typing import List

router = APIRouter(tags=["message"])    

@router.get(
    "/get_messages_for_blackboard",
    responses={
        404: {"description": "Project not found"},
        500: {"description": "Internal server error"}
    }
)
def get_messages_for_blackboard(
    blackboard_id: int,
    facade: MessageFacade = Depends(get_message_facade)
) -> List[Message]:
    try:
        messages = facade.get_messages_for_blackboard(blackboard_id=blackboard_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting messages: {str(e)}"
        )

    if messages is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Messages for blackboard '{blackboard_id}' not found"
        )

    return messages

@router.post(
    "/add_message",
    responses={
        500: {"description": "Internal server error"}
    }
)
def add_message(
    message: Message,
    facade: MessageFacade = Depends(get_message_facade)
) -> Message:
    return facade.add_message(message)



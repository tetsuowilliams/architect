from app.facades.blackboard_facade import get_blackboard_facade, BlackboardFacade
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.blackboard_api.blackboard import Blackboard

router = APIRouter(tags=["blackboard"])    

@router.get(
    "/get_blackboard_with_id",
    responses={
        404: {"description": "Blackboard not found"},
        500: {"description": "Internal server error"}
    }
)
def get_blackboard(
    id: int,
    facade: BlackboardFacade = Depends(get_blackboard_facade)
) -> Blackboard:
    try:
        blackboard = facade.get_blackboard_with_id(id=id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting blackboard: {str(e)}"
        )

    if blackboard is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blackboard '{id}' not found"
        )

    return blackboard

from app.facades.project_facade import get_project_facade, ProjectFacade
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.project_api.project import Project, ProjectTree
from typing import List

router = APIRouter(tags=["project"])    

@router.get(
    "/get_project_tree_with_id",
    responses={
        404: {"description": "Project not found"},
        500: {"description": "Internal server error"}
    }
)
def get_project_tree(
    id: int,
    facade: ProjectFacade = Depends(get_project_facade)
) -> ProjectTree:
    try:
        project = facade.get_project_tree_with_id(id=id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting project: {str(e)}"
        )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project '{id}' not found"
        )

    return project

@router.get(
    "/get_all_projects",
    responses={
        500: {"description": "Internal server error"}
    }
)
def get_all_projects(
    facade: ProjectFacade = Depends(get_project_facade)
) -> List[Project]:
    return facade.get_all_projects()

@router.options("/get_all_projects")
def options_get_all_projects():
    """Handle OPTIONS request for CORS preflight"""
    return {}


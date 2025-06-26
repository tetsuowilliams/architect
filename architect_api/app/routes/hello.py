from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def hello_world():
    """
    Hello World endpoint
    """
    return {"message": "Hello, World!"}

@router.get("/{name}")
async def hello_name(name: str):
    """
    Personalized hello endpoint
    """
    return {"message": f"Hello, {name}!"} 
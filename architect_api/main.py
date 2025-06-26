from fastapi import FastAPI
import uvicorn
from app.routes import blackboard_api

app = FastAPI(
    title="Architect API",
    description="A FastAPI service for the Architect project",
    version="1.0.0"
)

# Include routers
app.include_router(blackboard_api.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Architect API"}

if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=8000) 
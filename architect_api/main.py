from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import blackboard_api, project_api, message_api

app = FastAPI(
    title="Architect API",
    description="A FastAPI service for the Architect project",
    version="1.0.0"
)

# Configure CORS - this should be added BEFORE other middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Include routers
app.include_router(blackboard_api.router, prefix="/api/v1")
app.include_router(project_api.router, prefix="/api/v1")
app.include_router(message_api.router, prefix="/api/v1")
@app.get("/")
async def root():
    return {"message": "Welcome to Architect API"}

if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=8000) 
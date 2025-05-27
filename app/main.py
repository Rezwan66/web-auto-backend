from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv # Explicit import
load_dotenv()  # Call the function

from app.routes import form_filling_routes, llm_routes

app=FastAPI()

# Allow CORS (for frontend-backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import all route files
app.include_router(form_filling_routes.router)
app.include_router(llm_routes.router)

# Mock database (replace with real DB later)
fake_db = []

# Global home endpoint
@app.get("/")
async def root():
    return {"message": "Backend is running on port 8000"}

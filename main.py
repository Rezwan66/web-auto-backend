from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app=FastAPI()

# Allow CORS (for frontend-backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database (replace with real DB later)
fake_db = []

# Global home endpoint
@app.get("/")
async def root():
    return {"message": "Backend is running on port 8000"}

# Example GET endpoint for testing
@app.get("/get-form-data")
async def get_form_data():
    return {"data": "This is data from the backend GET endpoint."}

# Example POST endpoint to receive form data from UI
class FormData(BaseModel):
    title: str
    details: str

@app.post("/submit-form")
async def submit_form(data: FormData):
    # For now, just echo the data back to frontend
    return {
        "status": "success",
        "received": {
            "title": data.title,
            "details": data.details
        }
    }

@app.post('/generate')
def generate(prompt: str):
    response=ollama.chat(model='codeqwen',messages=[{'role':'user','content':prompt}])
    return {'response':response['message']['content']}

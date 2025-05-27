from fastapi import APIRouter
import ollama

router = APIRouter()

# Using direct Ollama functions - less control
@router.post('/generate')
def generate(prompt: str):
    response=ollama.chat(model='codeqwen',messages=[{'role':'user','content':prompt}])
    return {'response':response['message']['content']}

# Using httpx / Requests - better control, flexibility
@router.post('/')

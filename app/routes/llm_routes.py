from fastapi import APIRouter
import ollama

router = APIRouter()

@router.post('/generate')
def generate(prompt: str):
    response=ollama.chat(model='codeqwen',messages=[{'role':'user','content':prompt}])
    return {'response':response['message']['content']}

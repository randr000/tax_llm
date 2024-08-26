from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import retrieve, chat
from pydantic import BaseModel
import uvicorn

load_dotenv()
UVICORN_HOST = os.getenv('UVICORN_HOST')
UVICORN_PORT = os.getenv('UVICORN_PORT')

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['POST'],
    allow_headers=['*']
)

qa = retrieve()

class Query(BaseModel):
    query: str
    response: str | None = None

@app.post('/query')
async def chat_with_doc(query: Query) -> Query:
    return {
        'query': query.query,
        'response': chat(qa, query.query)
    }

if __name__ == '__main__':
    uvicorn.run('app:app', host=UVICORN_HOST, port=UVICORN_PORT)
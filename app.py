from fastapi import FastAPI
from chat import retrieve, chat
from pydantic import BaseModel

app = FastAPI()

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
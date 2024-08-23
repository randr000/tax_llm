from fastapi import FastAPI
from chat import retrieve, chat


app = FastAPI()

@app.get('/query')
async def root():
    return {'message': 'hello world'}
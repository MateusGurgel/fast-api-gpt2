from fastapi import FastAPI
from routes.gpt2_router import gpt2_router

app = FastAPI()

app.include_router(gpt2_router)
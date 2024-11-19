from dtos.gpt2_dto import GPT2Question, GPT2Awnser
from services.gpt2_services import GPT2Services
from fastapi import APIRouter

gpt2_router = APIRouter()

@gpt2_router.post("/")
def generate_gpt2_awnser(question: GPT2Question) -> GPT2Awnser:
    awnser = GPT2Services.generate(question.question)
    return {"awnser": awnser}
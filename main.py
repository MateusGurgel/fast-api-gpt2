from fastapi import FastAPI

from gpt2_dto import GPT2Question, GPT2Awnser


from gpt2_services import GPT2Services


app = FastAPI()


@app.post("/")
def generate_gpt2_awnser(question: GPT2Question) -> GPT2Awnser:
    awnser = GPT2Services.generate(question.question)
    return {"awnser": awnser}
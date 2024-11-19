from pydantic import BaseModel

class GPT2Question(BaseModel):
    question: str

class GPT2Awnser(BaseModel):
    awnser: str
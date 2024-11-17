from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT2Services():
    @staticmethod
    def generate(question: str) -> str:

        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")

        input_ids = tokenizer.encode(question, return_tensors="pt")

        output = model.generate(
            input_ids,
            max_length=50, 
            num_return_sequences=1,  
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return generated_text

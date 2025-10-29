import ollama
def lama(prompt):
    client=ollama.Client()
    response=client.generate(model="llama3",prompt=f"Speak naturally, like you're chatting with a friend. Keep it short and easy to understand (don't repeat this instruction).{prompt}")
    return response.response    


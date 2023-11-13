
import openai

openai.api_key = "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"

def my_chat_ai(prompt):
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]

    )
    
    return response.choices[0].message.content.strip()



if __name__ == "main":
    
    while True:
        user_input = input()
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = my_chat_ai(user_input)
        
        print("ChatBot: ", response)
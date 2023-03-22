import os
import openai

MAX_TOKENS=50

class ChatGPTClient:
    def __init__(self):
        # Set up OpenAI API credentials
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        self.model = "gpt-3.5-turbo"

        # ChatGpt doesn't keep track of a conversation. We have to send it the whole conversation each time.
        self.messages = [{"role": "system", "content": "You are a bot built to help users find and create reservations to restaurants."}]
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages= self.messages,
            max_tokens=MAX_TOKENS
        )
        
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})

    def send_message(self, message):
        print("DEBUG: messages = ", self.messages)

        self.messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            max_tokens=MAX_TOKENS,
        )
        
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"].content

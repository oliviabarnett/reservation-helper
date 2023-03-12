import os
import openai

from flask import Flask, render_template, request


class Chat:
    def __init__(self):
        # Set up OpenAI API credentials
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        self.model = "gpt-3.5-turbo"

        # ChatGpt doesn't keep track of a conversation. We have to send it the whole conversation each time.
        self.messages = [{"role": "system", "content": "You are a friendly assistant bot built to help users find and create reservations to restaurants"}]
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages= self.messages,
            max_tokens=20
        )
        
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})

    def send_message(self, message):

        self.messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            max_tokens=20,
        )
        
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"].content

def app_set_up(test_config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passged in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

def create_app(test_config=None):   

    # create and configure the app
    app = app_set_up(test_config)

    # Set up chat with chatGpt
    chatGpt = Chat()


    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/chat", methods=["POST"])
    def chat():
        user_input = request.form["input_text"]

        bot_response = chatGpt.send_message(user_input)

        # Return the bot's response as a JSON object
        return {"response": bot_response}


    return app







    
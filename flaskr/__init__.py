import os
import openai
from datetime import date
from flask import Flask, render_template, request

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

class ResyClient:

    # http://subzerocbd.info/#introduction
    def __init__(self):
        self.baseUrl = "https://api.resy.com"

        # TODO: where do I get these
        self.headers = {
            'X-Resy-Auth-Token': os.getenv("RESY_AUTH_TOKEN"),
            'Authorization': os.getenv("RESY_API_KEY")
        }


    # TODO: pass in date/time + location?
    def findOpenReservations(partySize):
        day = date.today().strftime("%Y/%m/%d")
        params = {
            'lat': '40.696235726060294',
            'long': '-73.97968099999999',
            'day': day,
            'party_size': str(partySize)
        }
        response = requests.get(url, params=params, headers=headers)



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

    chatGptClient = ChatGPTClient()
    resyClient = ResyClient()


    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/chat", methods=["POST"])
    def chat():

        # TODO: We somehow need to take this input, determine if enough information has been given yet to make a call into resy and retrieve information
        # Perhaps use another ChatGPT client that only goes from english text --> resy api calls? Then return that info, feed it into the 
        # other chat gpt client which will convert from json resy data --> english response?
        user_input = request.form["input_text"]


        bot_response = chatGptClient.send_message(user_input)
        


        return {"response": bot_response}


    return app







    
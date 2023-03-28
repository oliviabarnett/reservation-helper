
from flask import Flask, render_template, request
import os
from flaskr.models.ChatGPTClient import ChatGPTClient
from flaskr.models.ResyClient import ResyClient


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

    chatGptClient = ChatGPTClient("You are a bot built to help users find and create reservations to restaurants.")

    resyClient = ResyClient()


    @app.route('/find-res')
    def findRes():
        restaurants_with_availability = resyClient.find_open_reservations(2)
        restaurants_with_availability_str = '; '.join(r.to_string() for r in restaurants_with_availability)
        return restaurants_with_availability_str


    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/chat", methods=["POST"])
    def chat():

        # TODO: We somehow need to take this input, determine if enough information has been given yet to make a call into resy and retrieve information
        # Perhaps use another ChatGPT client that only goes from english text --> resy api calls? Then return that info, feed it into the 
        # other chat gpt client which will convert from json resy data --> english response?
        user_input = request.form["input_text"]

        parsed_info = InputParser(user_input)

        result = parsed_info.extract_from_user_input()

        chat_bot_response = chatGptClient.send_message(user_input)



        print("<INFO BOT>")
        print(info_bot_response)


        return {"response": chat_bot_response}


    return app




    
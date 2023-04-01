
from flask import Flask, render_template, request
import os
from flaskr.models.ChatGPTClient import ChatGPTClient
from flaskr.models.ResyClient import ResyClient
from flaskr.models.InputParser import InputParser


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
    input_fine_tuned_model = os.environ.get('CUSTOM_FINE_TUNED_MODEL')
    if not input_fine_tuned_model:
        raise ValueError("Fine tuned model name required!")

    # create and configure the app
    app = app_set_up(test_config)

    chatGptClient = ChatGPTClient("You are a bot built to help users find and create reservations to restaurants.", "gpt-3.5-turbo")
    resyClient = ResyClient()
    parsed_info = InputParser(input_fine_tuned_model)


    @app.route('/')
    def home():
        input_string = request.args.get('string-param')
        return render_template("home.html")

    @app.route("/chat", methods=["POST"])
    def chat():

        user_input = request.form["input_text"]

        # This does not work. We need to be able to process user input
        # and understand what needs to be called into resy..
        result = parsed_info.extract_from_user_input(user_input)
        resyClient.find_open_reservations(result)


        chat_bot_response = chatGptClient.send_message(user_input)

        return {"response": chat_bot_response}


    return app




    
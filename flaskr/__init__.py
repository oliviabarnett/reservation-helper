import os
import openai

from flask import Flask, render_template, request

def create_app(test_config=None):


    # TODO: Figure out secret management service
    # Currently set manually using env vars
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_engine = "davinci"

    # create and configure the app
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

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/chat", methods=["POST"])
    def chat():
        # Get the user input from the form data
        user_input = request.form["input_text"]
        print("<OB> user input = ", user_input)

        # Use the OpenAI API to generate a response to the user input
        completion = openai.Completion()

        response = completion.create(
            engine=model_engine,
            prompt=user_input,
            max_tokens=50,
            temperature=0.5,
        )
        print("<OB> response = ", response)
        bot_response = response.choices[0].text.strip()

        # Return the bot's response as a JSON object
        return {"response": bot_response}


    return app







    
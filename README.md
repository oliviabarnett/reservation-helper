# reservation-helper
resy &amp; chatgpt integration


# installation and set up:
Ensure you have python3 installed

create a virtual env with `python3 -m venv venv` (if the folder venv does not already exist)

run `source venv/bin/activate` to activate the virtual environment. You should now see "(venv)" on the left hand side of your screen.

run `pip install -r requirements.txt` and `python setup.py install` to install dependencies

train model for use:

(warning! This will cost money)
run: `openai api fine_tunes.create -t flaskr/resources/parsingModelTraining_prepared.jsonl -m davinci --suffix "reservation data parser v1"`

This will use your api key and fine tune a model for use in this app.

run: openai api fine_tunes.list to get the name of your model for input as an env variable as described below. For example, my model name was "davinci:ft-personal:reservation-data-parser-v1-2023-04-01-21-39-17"

set your environment variables. You will need:
1. export OPENAI_API_KEY="your api key" 
2. export RESY_API_KEY="your api key"
3. export CUSTOM_FINE_TUNED_MODEL="your trained model name"


run `flask --app flaskr run --debug` and go to listed url 


# testing
run `pytest tests` from root directory
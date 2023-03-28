# reservation-helper
resy &amp; chatgpt integration


# installation and running:
Ensure you have python3 installed

create a virtual env with `python3 -m venv venv` (if the folder venv does not already exist)

run `source venv/bin/activate` to activate the virtual environment. You should now see "(venv)" on the left hand side of your screen.

run `pip install -r requirements.txt` and `python setup.py install` to install dependencies

set your environment variables. You will need:
1. OPENAI_API_KEY env variable -- need to go get this from open ai's website
2. RESY_API_KEY

run `flask --app flaskr run --debug` and go to listed url 


# testing
run `pytest tests` from root directory
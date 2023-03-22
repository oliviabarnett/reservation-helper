# reservation-helper
resy &amp; chatgpt integration


# installation and running:
Ensure you have python3 installed

create a virtual env with `python3 -m venv venv` (if the folder venv does not already exist)

run `source venv/bin/activate` to activate the virtual environment. You should now see "(venv)" on the left hand side of your screen.

within that env install flask and open ai: `pip install Flask` `pip install openai`

set your environment variables. You will need:
1. OPENAI_API_KEY env variable -- need to go get this from open ai's website
2. RESY_API_KEY

run `flask --app flaskr run --debug`

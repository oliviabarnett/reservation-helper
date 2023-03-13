# reservation-helper
resy &amp; chatgpt integration


# installation and running:
Ensure you have python3 installed

create a virtual env with
  `python3 -m venv venv`
within that env install flask and open ai: 
  `pip install Flask` 
  `pip install openai`

set your secret OPENAI_API_KEY env variable
  get your own OpenAI key from open ai's website (instructions)
  edit your environment variable file (.bash

then run 
  `flask --app flaskr run --debug`

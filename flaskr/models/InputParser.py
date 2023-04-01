import spacy
from flaskr.models.ChatGPTClient import ChatGPTClient

class InputParser:
    def __init__(self, model):
        self.nlp = spacy.load("en_core_web_sm")

        # Surprise! Using chat gpt behind the scenes.
        initiationMessage = "You are a tool for extracting specific info from text to json. I will give you a text input and you will extract pertinent information and return text arguments as json. The output you respond should ONLY be json exactly following the below json format. Do not return anything else. If no information cannot be extracted from the given input, return an empty json string."
        
        # TODO: Fix this! Not working
        # print("model " + model)
        # self.parsingClient = ChatGPTClient(initiationMessage, model)


    def extract_from_user_input(self, user_input): 
            doc = self.nlp(user_input)

            # Extract the desired cuisine, location, time, and party size
            cuisine = ""
            location = ""
            date = ""
            party_size = ""

            
            # FML this doesn't work
            # I may need to literally train spacy to extract the data I want
            # Or I can use another chatgpt chat to extract this data
            for token in doc:
                print(token.ent_type_)
                if token.pos_ == "NOUN" and "food" in token.text:
                    cuisine = token.text
                if token.ent_type_ == "GPE":
                    location = token.text
                if token.ent_type_ == "TIME":
                    date = token.text
                if token.pos_ == "NUM" and "person" in token.text:
                    party_size = token.text
            return ResyRequestInfo(cuisine, location, date, party_size)

class ResyRequestInfo:
    def __init__(self, cuisine, location, date, party_size):
        self.cuisine = cuisine
        self.location = location
        self.date = date
        self.party_size = party_size

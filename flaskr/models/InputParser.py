import spacy

class InputParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

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

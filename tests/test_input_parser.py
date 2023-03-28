import pytest

from flaskr.models.InputParser import InputParser
from flaskr.models.InputParser import ResyRequestInfo

def test_extract_from_user_input():
    user_input = "I want sushi in West Village around 7pm for 4 people"
    parser = InputParser()

    expected_output = ResyRequestInfo("sushi", "west village", "2023-04-01", "4")
    actual_output = parser.extract_from_user_input(user_input)
    print(actual_output.cuisine, actual_output.location, actual_output.date, actual_output.party_size)

    assert actual_output == expected_output

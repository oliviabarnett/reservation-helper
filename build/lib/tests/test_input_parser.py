import pytest

from flaskr.models.InputParser import InputParser

def test_extract_from_user_input():
    parser = InputParser("I want sushi in West Village around 7pm for 4 people")

    expected_output = ResyRequestInfo("sushi", "west village", "2023-04-01", "4")

    assert parser.extract_from_user_input() == expected_output

import json
from random import randint

def newGame():
    with open("madlib.json") as f:
        madlibAPI =  json.load(f)
    madlibAPI = madlibAPI["templates"]
    randomNum = randint(0, len(madlibAPI) - 1)
    madlib = madlibAPI[randomNum]
    questions = madlib["blanks"]
    story = madlib["value"]
    title = madlib["title"]
    return { "responses": [], "questions": madlib["blanks"], "story": madlib["value"], "title": madlib["title"] }
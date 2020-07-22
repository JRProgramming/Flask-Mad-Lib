from flask import Flask, render_template, request
import requests
app = Flask(__name__)

responses = []
madlibAPI = requests.get("http://madlibz.herokuapp.com/api/random?minLength=2")
questions = madlibAPI.json()["blanks"]
story = madlibAPI.json()["value"]
title = madlibAPI.json()["title"]
form = "<input type='text' name='response'><input type='submit'><br>"
error = "<br><strong style='color: red;'>Please type something into the textfield</strong>"

@app.route("/")
def madlib():
    global questions, responses, story, title, form
    if request.args.get("response") and len(str(request.args.get("response")).strip()) != 0:
        responses.append(request.args.get("response"))
        if len(responses) == len(questions):
            storyString = ""
            for index, question in enumerate(story):
                if index < len(responses):
                    if index != 0:
                        responses[index] = responses[index].lower()
                    storyString += question + responses[index]
                else: 
                    if index != len(story) - 1:
                        storyString += question
            return render_template("index.html", title=title, story=storyString)
        return render_template("index.html", form=form, partOfSpeech=questions[len(responses)])
    elif len(request.args) != 0:
        return render_template("index.html", form=form, error=error, partOfSpeech=questions[len(responses)])
    else:
        newGame()
        return render_template("index.html", form=form, partOfSpeech=questions[0])

def newGame():
    global responses, madlibAPI, questions, story, title
    responses = []
    madlibAPI = requests.get("http://madlibz.herokuapp.com/api/random?minLength=2")
    questions = madlibAPI.json()["blanks"]
    story = madlibAPI.json()["value"]
    title = madlibAPI.json()["title"]

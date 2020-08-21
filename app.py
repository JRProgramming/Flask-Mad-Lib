from flask import Flask, render_template, request
from src.newGame import newGame
from src.generateStory import generateStory
from random import randint
import json
app = Flask(__name__)

responses = []
questions = []
story = ""
title = ""
form = "<input type='text' name='response'><input type='submit'><br>"
error = "<br><strong style='color: red;'>Please type something into the textfield</strong>"

@app.route("/", methods=["GET","POST"])
def madlib():
    global questions, responses, story, title, form, error
    if request.form.get("restart") or len(questions) == 0:
        output = newGame()
        responses, questions, story, title = output.values()
        return render_template("index.html", form=form, partOfSpeech=questions[0])
    if request.method == "POST" and len(str(request.form.get("response")).strip()) != 0:
        responses.append(request.form.get("response"))
        if len(responses) == len(questions):
            storyString = generateStory(responses, story)
            return render_template("index.html", title=title, story=storyString)
        return render_template("index.html", form=form, partOfSpeech=questions[len(responses)])
    return render_template("index.html", form=form, error=error, partOfSpeech=questions[len(responses)])
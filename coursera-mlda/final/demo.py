# -*- coding: utf-8 -*-
__author__ = 'onion_bass'

from flask import Flask, request, render_template
from sentiment_classifier import SentimentClassifier

import webbrowser

app = Flask(__name__)
classifier = SentimentClassifier()
print("Done")


@app.route("/", methods=["POST", "GET"])
def index(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
    print(text)
    prediction_message = classifier.get_prediction_message(text)
    return render_template('index.html', text=text,
                           prediction_message=prediction_message)


if __name__ == "__main__":
    webbrowser.open("http://localhost:5000/")
    app.run(debug=False)

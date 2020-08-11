from app import app
from flask import render_template, flash, redirect, url_for, session, request
from flask import jsonify
import nltk
from nltk.corpus import words
import random
import pickle
import tensorflow as tf

nltk.download("words")
cap_corpus = [word for word in words.words() if word[0:3].lower() == "cap"]

model = tf.keras.models.load_model("./nlp/models/model.h5")
with open("./nlp/models/tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)


def determine_cap(model, tokenizer, query):
    test_seq = tokenizer.texts_to_sequences([query])
    return model.predict(test_seq)[0]


@app.route("/cap", methods=["POST"])
def getModelsAndAssets():
    json = request.get_json()
    print(len(cap_corpus))

    output = determine_cap(model, tokenizer, json["input"])
    output = 0 if output < 0.5 else 1

    cap_word = cap_corpus[random.randint(0, len(cap_corpus))]
    cap_word = cap_word[:3].upper() + cap_word[3:]

    if output > 0.5:
        cap_word = "no-" + cap_word

    return jsonify({"response": cap_word})


@app.route("/capchain", methods=["GET"])
def getCapChain():
    return jsonify({"response": "test"})


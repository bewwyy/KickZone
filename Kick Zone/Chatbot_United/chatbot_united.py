import json
import random
import pickle
import numpy
import nltk
import keras
import keras.models
import os


def main(message):
    base_path = os.path.dirname(__file__)
    intents = load_intents(os.path.join(base_path, "intents.json"))
    words = load_pkl(os.path.join(base_path, "words.pkl"))
    classes = load_pkl(os.path.join(base_path, "classes.pkl"))
    model = keras.models.load_model(os.path.join(base_path, "chatbot_model.h5"))

    ints = predict_class(message, model, words, classes)
    res = get_response(ints, intents)
    return f"{res}"


def load_intents(path):
    with open(path, "r", encoding="UTF-8") as data_file:
        return json.load(data_file)


def load_pkl(path):
    with open(path, "rb") as file:
        return pickle.load(file)


def clean_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    words = [nltk.WordNetLemmatizer().lemmatize(word.lower()) for word in words]
    return words


def create_bag_of_words(sentence, words):
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)

    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1

    return numpy.array(bag)


def predict_class(sentence, model, words, classes):
    bag_of_words = create_bag_of_words(sentence, words)
    res = model.predict(numpy.array([bag_of_words]))[0]
    threshold = 0.3

    results = []
    for i, r in enumerate(res):
        if r > threshold:
            results.append([i, r])
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for result in results:
        return_list.append({"intent": classes[result[0]], "prob": str(result[1])})
    return return_list


def get_response(return_list, intents):
    error_caused = False
    try:
        tag = return_list[0]["intent"]
    except IndexError:
        error_caused = True

    intents_list = intents["intents"]

    result = ""
    if error_caused:
        return "I didn't get that! Please ask me another question and I will try my best to answer!"
    for i in intents_list:
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            break
    return result
# this python file, loads the trained model into streamlit.py
import keras
import pickle


def load_model(data):
    model = keras.models.load_model(data)
    return model

def load_tokeniser(token):
    with open(token, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

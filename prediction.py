# this python file, loads the trained model into streamlit.py
import keras
import pickle

"""
This code defines two functions: load_model() and
load_tokeniser().
"""
def load_model(data):
    """
    load_model() takes in a parameter 'data' which
    is a path to a model file, and uses the Keras
    library to load the model from the file.
    It then returns the loaded model.

    """
    model = keras.models.load_model(data)
    return model

def load_tokeniser(token):
    """
    load_tokeniser() takes in a parameter 'token' which is a
    path to a tokeniser file, and uses the pickle library to
    load the tokeniser from the file. It then returns the
    loaded tokeniser.

    """
    with open(token, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

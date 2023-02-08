
# import modules
import pickle
import numpy as np
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import keras
from prediction import load_model, load_tokeniser

#import model
model = load_model('my_model.h5')
tokenizer = load_tokeniser('tokenizer.pickle')



def make_lyrics(seed_text, next_words):
    """
    This function creates lyrics based on a given seed text
    and the number of words to generate. It uses a tokenizer
    to convert the seed text into sequences of numbers and
    pads them to a maximum sequence length of 88.
    It then reshapes the token list into a 3D array which
    is used as an input for the model. The model then predicts
    the next word and returns it as part of the lyrics.

    """
    max_sequence_len = 88
    pred_index=[]
    for i in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list],
                     maxlen=max_sequence_len-1,padding='pre')
        #print(token_list.shape)
        token_list = np.reshape(token_list, (1, max_sequence_len-1, 1))
        predicted = model.predict(token_list, verbose=0)
        predicted_index =  np.argmax(predicted)
        pred_index.append(predicted_index)




        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break
        seed_text += " " + output_word
    #print(seed_text)
    return seed_text

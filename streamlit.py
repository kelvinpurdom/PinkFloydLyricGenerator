# import packages
import streamlit as st
import pandas as pd
from model import make_lyrics



seed = st.text_input('seed text:', '')
output_length = st.number_input('Sentence length:', min_value=1, max_value=88, value=10, step=1)


st.text(make_lyrics(seed, output_length))

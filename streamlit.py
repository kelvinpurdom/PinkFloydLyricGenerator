# import packages
import streamlit as st
import pandas as pd
from model import make_lyrics



seed = st.text_input('seed text:', '')


st.text(make_lyrics(seed, 7))

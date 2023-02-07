# import packages
import streamlit as st
import pandas as pd
from prediction import predict
from model import make_lyrics



title = st.text_input('seed text:', '')


st.text(make_lyrics(title, 7))

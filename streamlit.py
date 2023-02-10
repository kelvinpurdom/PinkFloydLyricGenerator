# import packages
import streamlit as st
import pandas as pd
from model import make_lyrics
import webbrowser

"""
This code sets the page title of a Streamlit page to
"Pink Floyd Lyric Generator". It also hides the default
menu and footer from the page, adds a header and subheader
to the page, adds a button that links to
Kelvin Purdom's Github, adds an image of Pink Floyd,
and adds a text input for users to enter words which will
be used to generate new Pink Floyd lyrics.
"""

# set tab button
#st.set_page_config(page_title='Pink Floyd Lyric Generator')

# remove menu and footer from streamlit
hide_default_format = """
       <style>

       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center'>Pink Floyd Lyric Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Created by Kelvin Purdom</h3>", unsafe_allow_html=True)


url = 'https://github.com/kelvinpurdom'
if st.button('Kelvins Github'):
    webbrowser.open_new_tab(url)
st.image("""https://www.grunge.com/img/gallery/the-untold-truth-of-pink-floyd/intro-1626917943.webp""")

st.markdown("<h6 style='text-align: center'>Photo: Michael Ochs Archives/Getty Images</h6>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Enter some words below to create some new Pink Floyd Lyrics:</h3>", unsafe_allow_html=True)
seed = st.text_input('', '')
st.subheader(make_lyrics(seed, 20))

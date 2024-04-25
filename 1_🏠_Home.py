import streamlit as st
import git
import os
import base64
st.set_page_config(
  page_title="Policumbent",
  page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLBnwH3bm6RwJvsl1-w4PDKxydP6wUIJNDs9pMaI1lpw&s", 
)
#code to hide streamlit normal view
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </stile>
"""


st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("home page")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
background-color: rgb(255, 191, 71)
}}
[data-testid="stHeader"] {{
background: rgba(255,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


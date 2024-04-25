import streamlit as st

st.set_page_config(
  page_title="InclusED",
  page_icon="https://github.com/SamVia/exchange-site/blob/main/logo.png?raw=true", 
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
st.title("INFO:")

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

col1, col2 = st.columns(2)
col1.write("## Our Work:\nwe provide this and this\nthis\nthis")
command = """
<div style="text-align:center; border:4px; border-radius:5px;">
  <img src="https://www.verywellfamily.com/thmb/zzxxNlOAiqHASXAMVdlQSS7wQbs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyEchoSummerKidsBubbles-56aa2ed75f9b58b7d001a147.jpg" alt="Image Description" style="width: 400px; height: auto;" />
    
  </div>
"""
col2.markdown(command, unsafe_allow_html=True)
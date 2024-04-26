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

col1, col2 = st.columns(2)
col1.write("## About US:\n")
pres_text="""
    <head>
    <style>
    .custom-text {
      /* Dimension Properties */
      width: 400px;
      height: auto;

      /* Padding and Margin Properties */
      padding: 20px;
      margin: 10px;

      /* Border Properties */
      border-width: 2px;
      border-style: solid;
      border-color: black;
      border-radius: 10px;

      /* Background Properties */
      background-color: rgba(0,0,0,0.1);

      /* Text Properties */
      color: white;
      text-align: center;
      font-size: 16px;

      /* Display Properties */
      display: block;

      /* Positioning Properties */
      position: relative;
      left:-160px;

      /* Transition Properties */
      transition: all 0.5s ease;
    }
  </style>
  </head>
  <body>
    <div class="custom-text">
    Welcome to InclusED, where we champion inclusivity, empowerment, and opportunity for youths of all backgrounds and abilities. At our core, we embrace the neurodivergent community, guiding and supporting youths as they navigate the unique landscape of the neurodivergent world. Whether individuals are on the autism spectrum or identify with other neurodivergent traits, we provide a nurturing environment to foster personal growth and success. Our mission extends beyond mere inclusion; we're dedicated to equipping these young individuals with the tools and resources they need to excel in both their academic pursuits and future careers. Moreover, we're committed to fostering understanding and acceptance in the broader workforce, advocating for accommodations and adjustments that allow neurodivergent talents to shine. Join us as we pave the way for a more inclusive and supportive society, one where every youth has the opportunity to thrive.
</div>
</body>  
    
    
    """
    
col1.markdown(pres_text, unsafe_allow_html=True)


command = """
<div style="text-align:center">
  <img src="https://github.com/SamVia/exchange-site/blob/main/logo.png?raw=true" alt="Image Description" style="width: 400px; height: auto;" />
</div>
"""
command = """
                <div class="image-container">
    <img src="https://github.com/SamVia/exchange-site/blob/main/logo.png?raw=true" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:0px;
    top:100px;
    /*box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);*/">
</div>
                
                
            """
col2.markdown(command, unsafe_allow_html=True)
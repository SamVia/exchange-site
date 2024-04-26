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

# col1, col2 = st.columns(2)
# col1.write("## Our Work:\nwe provide this and this\nthis\nthis")
# command = """
# <div style="text-align:center; border:4px; border-radius:5px;">
#   <img src="https://www.verywellfamily.com/thmb/zzxxNlOAiqHASXAMVdlQSS7wQbs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyEchoSummerKidsBubbles-56aa2ed75f9b58b7d001a147.jpg" alt="Image Description" style="width: 400px; height: auto;" />
    
#   </div>
# """
col1, col2 = st.columns(2)
col1.write("## Our Cause:\n")
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
    <p>
<strong>Embracing Neurodiversity: Empowering Youths for Success</strong>
</p>

<p>
At InclusED, we believe that every youth, regardless of their neurodivergent traits, deserves the opportunity to thrive. Our organization is built upon the foundational principle of embracing neurodiversity — recognizing and celebrating the unique strengths, perspectives, and talents that each individual brings to the table.
</p>

<p>
<strong>Understanding the Neurodivergent World</strong>
</p>

<p>
Our journey begins with a deep dive into the neurodivergent world. We understand that navigating this landscape can be complex, especially for youths who may be on the autism spectrum or possess other neurodivergent traits. Through educational programs, workshops, and resources, we provide a comprehensive understanding of neurodiversity, helping youths and their families navigate the challenges and opportunities it presents.
</p>

<p>
<strong>Guiding Pathways to Success</strong>
</p>

<p>
Once immersed in our community, we're dedicated to helping youths find their path to success. Whether it's through academic support, vocational training, or career guidance, we offer personalized assistance tailored to each individual's needs and aspirations. Our goal is not just to help youths succeed, but to empower them to thrive in their chosen pursuits.
</p>

<p>
<strong>Empowering Through Education and Employment</strong>
</p>

<p>
Education and employment are pillars of empowerment, and we're committed to ensuring that neurodivergent youths have access to both. From tutoring and study skills development to job readiness training and internship opportunities, we equip youths with the skills, confidence, and resources they need to pursue their academic and career goals with determination and resilience.
</p>

<p>
<strong>Advocating for Inclusive Work Environments</strong>
</p>

<p>
Beyond individual support, we're passionate about creating systemic change. We work tirelessly to educate employers and businesses about the benefits of neurodiversity in the workforce, advocating for inclusive hiring practices and workplace accommodations that enable neurodivergent talents to thrive. By fostering understanding and acceptance, we're breaking down barriers and building a more inclusive society for all.
</p>

<p>
<strong>Join Us in Empowering Neurodivergent Youths</strong>
</p>

<p>
At InclusED, we're more than just an organization — we're a community of advocates, mentors, and champions for neurodiversity. Together, we're paving the way for a future where every youth has the opportunity to reach their full potential, regardless of their neurodivergent traits. Join us in our mission to create a world where differences are celebrated, talents are nurtured, and all youths are empowered to shine.
</p>

</div>
</body>  
    
    
    """
    
col1.markdown(pres_text, unsafe_allow_html=True)



command = """
                <div class="image-container">
    <img src="https://www.verywellfamily.com/thmb/zzxxNlOAiqHASXAMVdlQSS7wQbs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyEchoSummerKidsBubbles-56aa2ed75f9b58b7d001a147.jpg" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:0px;
    top:400px;
    /*box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);*/">
</div>
                
                
            """
col2.markdown(command, unsafe_allow_html=True)


command2 = """
                <div class="image-container">
    <img src="https://previews.123rf.com/images/sbworld8/sbworld81206/sbworld8120600001/14108586-group-of-happy-children-with-thumbs-up-sign-isolated-on-white.jpg" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:0px;
    top:400px;
    /*box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);*/">
</div>
                
                
            """
col2.markdown(command2, unsafe_allow_html=True)

command3 = """
                <div class="image-container">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8SmQSMGRFdsaZyORgoklzdqvcB70-5h6fjgZMT2s7BA&s" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:0px;
    top:400px;
    /*box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);*/">
</div>
                
                
            """
col2.markdown(command3, unsafe_allow_html=True)

command4 = """
                <div class="image-container">
    <img src="https://www.vancopayments.com/hs-fs/hubfs/Graduation%20-%20Cap%20throw.png?width=1640&height=924&name=Graduation%20-%20Cap%20throw.png" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:0px;
    top:400px;
    /*box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);*/">
</div>
                
                
            """
col2.markdown(command4, unsafe_allow_html=True)


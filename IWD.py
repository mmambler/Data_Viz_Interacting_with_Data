import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

def BuildPage():

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    st.header("Part 3: How mental health relates to suicidal ideation in Indigenous and non-Indigenous populations?")

    HtmlFile = open("IWD_Part3.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 800, width = 900)

BuildPage()

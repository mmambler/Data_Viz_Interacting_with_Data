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
    
    st.header("Part 1: What proportion of Canadians identify as Indigenous?")

    HtmlFile = open("donut.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 800, width = 900)

    st.header("Part 2: Where are Indigenous populations in Canada?")

    HtmlFile = open("map.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 800, width = 900)

    st.header("Part 2 (Additional): Demographics of Top-3 Provinces in Terms of Indigenous Population")
    
    HtmlFile = open("subplots.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 800, width = 900)

    st.header("Part 3: How mental health relates to suicidal ideation in Indigenous and non-Indigenous populations?")

    HtmlFile = open("scatter.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 800, width = 900)

BuildPage()

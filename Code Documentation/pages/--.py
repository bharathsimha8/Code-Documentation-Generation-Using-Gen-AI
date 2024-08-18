import streamlit as st
st.set_page_config(
    page_title="Code Documentation",  
    page_icon=":rocket:",         
    layout="wide",                
    initial_sidebar_state="auto"  
)

html_text = "<h1 style='text-align: center; color: red;'>Sign out Successfully</h1>"


st.markdown(html_text, unsafe_allow_html=True)

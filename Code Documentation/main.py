import streamlit as st
import login
import signup

st.set_page_config(
    page_title="Code Documentation",  
    page_icon=":rocket:",         
    layout="wide",                
    initial_sidebar_state="auto"  
)


def login1():
    login.app()
    
    
def signup1():
    signup.app()
page_names_to_funcs = {
    "Login":login1,
    "Sign Up":signup1
}

selected_page = st.sidebar.selectbox("Select a Option", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
about=st.sidebar.button("About")
if about:
    st.switch_page('pages/___.py')



    
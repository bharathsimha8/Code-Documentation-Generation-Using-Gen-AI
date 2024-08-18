import streamlit as st
import database
st.set_page_config(
    page_title="Code Documentation",  
    page_icon=":rocket:",         
    layout="wide",                
    initial_sidebar_state="auto"  
)

email = st.session_state.get("email")  

signout = st.sidebar.toggle("Sign Out")
if signout:
    st.switch_page('pages/--.py')

history = database.geth(email)


if isinstance(history, list):
    for index, (response) in enumerate(history, start=1):
        if st.checkbox("Show Response", key=index):
            st.write("Response:")
            st.write(response)
st.markdown(
    """
    <style>
    .stButton>button {
        position: fixed;
        bottom: 0;
        right: -1%;
       
        transform: translateX(-50%);
        margin-bottom: 10px;
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


button_clicked = st.button("Back")
if button_clicked:
    st.switch_page("pages/_.py")

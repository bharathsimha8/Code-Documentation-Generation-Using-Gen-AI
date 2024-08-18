
import streamlit as st

import database as database

def app():
    st.title(':green[Sign Up]')
    email = st.text_input(':blue[Email]',placeholder='Enter the Email')
    name = st.text_input(':blue[Name]',placeholder='Enter the Name')
    password = st.text_input(':blue[Password]', placeholder="Enter the Password",type="password")
    retype_password = st.text_input(':blue[Retype Password]',placeholder="Retype the Password" ,type="password")
    if st.button("Sign Up"):
        if not (name and email and password and retype_password):
            st.warning("Please enter all fields")
        elif "@gmail.com" not in email:
            st.warning("Enter the Valid Email")
        elif len(name)<=3:
            st.warning("Name is too Short")
        elif len(password)<=6:
            st.warning("Password is too Short")
        elif password!=retype_password:
            st.warning("Password Mismatched")
        else:
            if database.check(email):
                st.warning("Email Already Exists!! Please Login")
            else:
                database.data(email,name,password)
                st.success("Sign Up Successfully")
                st.balloons()
              
                

        

       



                   
       
        


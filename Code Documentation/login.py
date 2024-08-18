import streamlit as st
import database as database



import time

def app():
     
     st.title(':red[Login Page]')
     email = st.text_input(':blue[Email]',placeholder="Enter the Email")
     password = st.text_input(':blue[Password]',placeholder="Enter the Password", type="password")
     
     if st.button("Log in"):
          if not (email and password):
            st.warning("Please Enter All Fields")
          elif "gmail.com" not in email:
            st.warning("Enter the Valid Email")
          else:
             if not (database.checkout(email,password)):
                st.warning("User not found!! Please Sign Up")
                
               
               
             else:
                st.toast("Login Successfully!!!")
                time.sleep(.8)
                st.session_state.email = email
                st.switch_page('pages/_.py')
                

                   
               
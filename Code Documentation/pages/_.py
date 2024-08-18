import openai
import os
from dotenv import load_dotenv
import streamlit as st
import time
import database
st.set_page_config(
    page_title="Code Documentation",  
    page_icon=":rocket:",         
    layout="wide",                
    initial_sidebar_state="auto"  
)
load_dotenv(override=True)
api_key = os.getenv('OPEN_API_KEY')
openai.api_key = api_key
def get_completion(prompt, text,model="gpt-3.5-turbo"):
            messages = [{"role": "user", "content": prompt}]
            with st.chat_message("user"):
              st.markdown(text)
            
          
            with st.chat_message("assistant"):
              message_placeholder = st.empty()
            with st.spinner("Generating....."):

                    response = openai.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=0
                    )
            response_message = response.choices[0].message.content
            return response_message
email = st.session_state.get("email")  
st.title("Code Documentation")           
input_text = st.text_area("Enter the code")
opt=['Comments for the code','Technical Documentation','Functional Documentation']
option=st.radio("Choose any one option",opt)
btn=st.button("Submit")
if btn:
    if input_text:  
      if option=='Comments for the code':
            prompt=f"""Given a code snippet, provide clear and concise comments to describe its functionality. Ensure that the comments are informative and easy to understand, helping other developers comprehend the purpose and logic of the code. Focus on explaining key components, operations, and any important considerations. Aim to make the comments readable and well-organized, enhancing the code's documentation and maintainability.Also provide algorithm name in first line.Also display the entire code along with comments.And also check the given code not be concepts of programming language if it then display The given code snippet is not provided. Please enter the code snippet.
            Review:```{input_text}```
              """
            response=get_completion(prompt,input_text)
            st.markdown(response)
            database.hist(email,option,response)
            download=response
            st.download_button("Download",download)
      elif option=='Technical Documentation':
            prompt =f"""Review the following code as per technical specifications and generate the required technical specification document along with build blocks for its functionality.List all the build blocks for the below code.Also provide algorithm name in the first line.
            Review:```{input_text}```
            """
            response=get_completion(prompt,input_text)
            st.markdown(response)
            database.hist(email,option,response)
            download=response
            st.download_button("Download",download)
      elif option=='Functional Documentation':
            prompt =f"""Please review the code below and provide suitable functional specifications for the developed functionality.List all the possible functional specs which the below code can cover.Generate a functional specification document for the below code.
             Review:```{input_text}```
              """
            response=get_completion(prompt,input_text)
            st.markdown(response)
            database.hist(email,option,response)
            download=response
            st.download_button("Download",download)
    else:
       st.warning("Please Enter The Code!!!")


      




       
       
button_clicked = st.sidebar.button("History")
if button_clicked:
       st.switch_page("pages/__.py")
singout=st.sidebar.toggle("Sign Out")
if singout:
      st.switch_page("pages/--.py")
     









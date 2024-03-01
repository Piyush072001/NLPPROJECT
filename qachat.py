from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#FUNCTION TO LOAD GENAI MODEL AND GET RESPONSE

model= genai.GenerativeModel("gemini-pro")


#Chat Session Start:
# chat = model.start_chat(history=[]): This line starts a chat session using the 
# initialized model. The start_chat method is called on the model, and it likely 
# returns a chat object or session. The history parameter, which is set to an empty list ([])
# might represent the chat history.
chat=model.start_chat(history=[])

def get_gemini_response(question):
    # stream=true means it will generate response in chunks not all at once
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A demo")

st.header("Gemini LLM application")

# initialize session state  for chat history if it dose't exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
    

#it is a inbuilt function for taking input in streamlit

# text_input: A function in Streamlit used to create a text input box.

# "input": The first argument is the label or prompt for the text input box.
# In this case, it is set to "input".

# key="input": The key parameter is optional. It provides a way to uniquely identify
# the input element. If not specified, Streamlit will automatically generate a key.

    
input=st.text_input("Input:" , key="input")
submit=st.button("ask the question")

if submit and input:
    response =get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
    
st.subheader("The chat History is")
        
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

    

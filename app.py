from dotenv import load_dotenv
load_dotenv() ## loading all the environments variable

import streamlit as st 
import os
import google.generativeai as genai
st.title("Papa Here")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model and get respnses
# .py (Python Script):

# Format: It is a plain text file with a .py extension.
# Environment: .py files are traditional Python scripts. They are written in a text editor or an integrated development environment (IDE) and contain Python code.
# Execution: Code in .py files is executed sequentially, line by line. You run these scripts using a Python interpreter from the command line or an IDE.
# .ipynb (Jupyter Notebook):

# Format: It is a JSON-based file format containing both code and rich-text elements, including images, equations, and narrative text. It is associated with Jupyter Notebooks.
# Environment: Jupyter Notebooks provide an interactive computing environment. They are a mix of code cells and markdown cells, allowing for the integration of code and documentation in a single file.
# Execution: Code cells in .ipynb files can be executed independently, and the results are displayed inline. This makes it easy to experiment, visualize data, and share insights in a more interactive and exploratory way.
 
model=genai.GenerativeModel("gemini-pro")
 
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("THE RESPONSE IS")
    st.write(response)
    


    
      
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pprint
import google.generativeai as palm
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

# loading .env
load_dotenv()

# loading api_key .env variable
palm.configure(api_key=os.environ.get('API_KEY'))


# Side bar content
with st.sidebar:
    st.title("Chat with your PDF")
    st.markdown(
        """
    # About
    ### This LLM powered app lets you chat with your pdf file. Built by using
                 
    - [Streamlit](https://www.streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [Palm API](https://makersuite.google.com/app/home)

"""
    )

    add_vertical_space(14)
    st.write("""Made by [Rahul Netkar](https://www.github.com/rahulNetkar)""")


def main():
    st.title("Welcome to Chat PDF")

    # upload pdf file
    pdf = st.file_uploader("Upload your pdf here", type="pdf")
    
    if pdf is not None:
        pass

if __name__ == "__main__":
    main()
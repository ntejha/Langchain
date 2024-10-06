import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2'] = "True"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")


##Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Your are a hepful assistant. Please respond to the question asked"),
        ("user","Wuestion:{question}")
    ]
)

##streamlit framework

st.title("Langchain Demo with Gemma2")
input_text = st.text_input("What quesion you have in mind?")

##Ollama Gemma2 model

llm = Ollama(model="gemma2:2b")
output_parder = StrOutputParser()
chain = prompt|llm|output_parder

st.write(chain.invoke({"question":input_text}))
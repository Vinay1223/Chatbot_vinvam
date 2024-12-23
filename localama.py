from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ['LANGCHAIN_TRACING_V2'] = 'true'
# os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')



## Prompt template

prompt = ChatPromptTemplate.from_messages(

[
    ('system', 'Your are a helpful assistant. Please respond to the user queries'),
    ('user', 'Question:{question}')
]
)

## Streamlit framework

st.title('Langchain Demo with LLama2 API')
input_text = st.text_input('Search the topic u want ')

## OpenAI llm
llm = Ollama(model = 'gemma')
output_parser = StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
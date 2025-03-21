import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

#### Load environment variables
load_dotenv()
###

# Environment setup
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the user queries.'),
        ('user', 'Question:{question}')
    ]
)

# Streamlit app configuration
st.set_page_config(
    page_title="LangChain Demo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar content
with st.sidebar:
    st.title("About")
    st.write(
        """
        🤖 **LangChain Demo App**  
        Powered by **LLama2 API** and **LangChain**.  
        Enter a question to get an AI-powered response.  
        """
    )
    st.markdown("### Useful Links")
    st.markdown("[LangChain Documentation](https://python.langchain.com)")
    st.markdown("[Streamlit Documentation](https://docs.streamlit.io)")

# App title
st.title("🤖 LangChain Demo with LLama2 API")
st.markdown("### Explore AI-powered responses. Type your question below or select a suggestion!")

# Suggestions for questions
suggested_questions = [
    "What is AI?",
    "How does LangChain work?",
    "Explain large language models.",
    "What are the applications of Generative AI?"
]

selected_question = st.selectbox("Choose a suggested question:", [""] + suggested_questions)

# Text input
input_text = st.text_input("Or type your own question:", placeholder="e.g., What is Generative AI?")

# LLM initialization
llm = Ollama(model='gemma')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Handle input and generate response
if input_text or selected_question:
    question = input_text if input_text else selected_question
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({'question': question})
            st.subheader("Response:")
            # Use expander for long responses
            with st.expander("Click to see the full response"):
                st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.write("🤝 Made with [Streamlit](https://streamlit.io) and ❤️ by [VINVAM]")

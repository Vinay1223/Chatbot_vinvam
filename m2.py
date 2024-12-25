import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Ensure the API key is loaded properly

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the user queries.'),
        ('user', 'Question:{question}')
    ]
)

# Streamlit app configuration
st.set_page_config(
    page_title="Intelligent-Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar content
with st.sidebar:
    st.title("About")
    st.write(
        """
        🤖 **VINVAM-BOT**  
        Powered by **Gemini API** and **LangChain**.  
        Enter a question to get an AI-powered response.  
        """
    )
    st.markdown("### Useful Links")
    st.markdown("[LangChain Documentation](https://python.langchain.com)")
    st.markdown("[Streamlit Documentation](https://docs.streamlit.io)")

# App title
st.title("🤖 VINVAM BOT ")
st.markdown("### Explore AI-powered responses. Type your question below or select a suggestion!")

# Suggestions for questions
suggested_questions = [
    "What is AI?",
    "How does LangChain work?",
    "Explain large language models.",
    "What are the applications of Generative AI?"
    'How old are you?'
]

selected_question = st.selectbox("Choose a suggested question:", [""] + suggested_questions)

# Text input
input_text = st.text_input("Or type your own question:", placeholder="e.g., What is Generative AI?")

# LLM initialization for Google Gemini
def generate_response(question: str):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with the appropriate model ID
    response = model.generate_content(question)
    return response.text

# Handle input and generate response
if input_text or selected_question:
    question = input_text if input_text else selected_question
    with st.spinner("Generating response..."):
        try:
            # Generate response using Gemini model
            response_text = generate_response(question)
            st.subheader("Response:")
            # Use expander for long responses
            with st.expander("Click to see the full response"):
                st.write(response_text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.write("🤝 Made with [Streamlit](https://streamlit.io) and ❤️ by [VINVAM]")

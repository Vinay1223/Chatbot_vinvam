# 🤖 VINVAM-BOT  
**VINVAM-BOT** is an AI-powered chatbot built with **Streamlit**, **Google Gemini API**, and **LangChain** to provide intelligent, conversational responses to user queries. This application leverages the power of generative AI models to handle natural language questions and provide meaningful responses in real time.

## 🚀 Features
- **AI-Powered Responses**: Uses Google's Gemini generative AI model to generate accurate and conversational responses.
- **Streamlit Interface**: A simple, user-friendly interface for users to interact with the bot.
- **Suggested Questions**: Includes predefined question suggestions to guide users.
- **LangChain Integration**: Utilizes LangChain's `ChatPromptTemplate` for structured and context-aware prompts.
- **Expandable Responses**: Responses are displayed in an expandable section for easy viewing of longer answers.
- **Customizable Sidebar**: Provides details about the bot and useful links to documentation.

## 📋 Requirements
To run this application, ensure you have the following installed:
- Python 3.8 or later
- Streamlit
- Google Gemini AI Python SDK (`google.generativeai`)
- LangChain Core
- Python `dotenv` for environment variable management

## 🔧 Setup
Follow these steps to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/vinvam-bot.git
   cd vinvam-bot
2. **Install Dependencies**: 
    ```bash
    pip install -r requirements.txt

3. **Set Up API Keys**:
    - Create a .env file in the root directory
    - Add your Google Gemini API key in the .env file:
    ```makefile
    GEMINI_API_KEY = your_google_gemini_api_key
4. **Run the Application**:
    ```bash
    streamlit run app.py
5. **Access the APP**:
    Open your browser and go to (`http://localhost:8501.`)
## 🛠 How it works
1. **Gemini API Configuration**:
    - The Google Gemini API key is loaded securely using the (`dotenv`) package.
    - The (`gemini-1.5-flash`) model is used to generate responses to user questions.
2. **Prompt Template**:
    - The bot uses LangChain's (`ChatPromptTemplate`) to structure prompts.
    - A system message ensures the AI behaves as a helpful assistant.
3. **User Interaction**:
    - Users can either select a predefined question from a dropdown or type their own query.
    - The input is processed, and the AI model generates a response in real time.
4. **Response Display**:
    - Short responses are shown directly.
    - Long responses are displayed in an expandable section for better readability.
5. **Error Handling**:
    - Comprehensive error handling ensures graceful handling of issues like missing API keys or invalid model IDs.
## 📚 File Structure
```bash
  vinvam-bot/
  |
  |--- app.py
  |--- .env
  |--- requirements.txt
  |--- README.md
```

## 🌟 Key Features Highlighted in the Code
- **Gemini API Integration**: The (`generate_response`) function uses the Gemini model to generate AI responses:
  ```bash
  def generate_response(question: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(question)
    return response.text
  ```
- **LangChain Prompt Template**: The (`ChatPromptTemplate`) Structures the input for a more intelligent response:
    ```python
  prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the user queries.'),
        ('user', 'Question:{question}')
    ]
    )
  ```
- **Streamlit Features**:
  - Interactive dropdown (`st.selectbox`) for suggested questions.
  - Real-time input field (`st.text_input`) for custom questions.
  - Expandable sections for long responses (`st.expander`).
## 🤝 **Contributing**
Contributions are welcome! If you encounter bugs or have feature requests, feel free to open an issue or submit a pull request. 

## 📄 **License**
This project is licensed under the MIT License. See the LICENSE file for details.

##❤️ **Acknowledgments**
- Streamlit for the beautiful UI framework.
- LangChain for prompt engineering tools.
- Google Gemini for the generative AI model.
-----



![image](https://github.com/user-attachments/assets/7412fa10-ab8d-4775-946a-8fab9f36bccc)


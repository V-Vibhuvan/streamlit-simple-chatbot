import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("💬 Generative AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize Ollama LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key = st.secrets["GROQ_API_KEY"],
    temperature=0.0
)

# Input box
user_prompt = st.chat_input("Ask chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    response = llm.invoke(
        [{"role": "system", "content": "You are a helpful assistant"},
         *st.session_state.chat_history]
    )

    assistant_response = response.content

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_response)


from asyncio import taskgroups
import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load .env relative to this file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

st.header("Research Tool")

api_key = os.getenv("Google_Gemini_API_KEY")

if not api_key:
    st.error("Google Gemini API Key not found. Please verify your .env file.")
    st.stop()

# Use supported model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    api_key=api_key,
    temperature=0.7
)

user_input = st.text_input("Enter your prompt:")

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Summarizing..."):
            result = model.invoke(user_input)
            
            # Extract plain text from response
            output_text = (
                result.text
                if hasattr(result, "text") and result.text
                else (result.content[0]["text"] if isinstance(result.content, list) else result.content)
            )
            try:
                st.write(output_text)
            except Exception as e:
                st.error(f"Error: {e}")

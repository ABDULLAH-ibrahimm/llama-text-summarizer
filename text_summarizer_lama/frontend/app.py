import streamlit as st
import requests

st.title("LLaMA Text Summarizer")

user_input = st.text_area("Enter your text here:")

if st.button("Summarize"):
    try:
        response = requests.post(
            "http://localhost:8000/summarize/",
            data={"text": user_input}
        )
        response.raise_for_status()  # Raise if HTTP error
        try:
            summary = response.json().get("summary", "Error generating summary.")
        except ValueError:
            summary = f"Invalid JSON from backend: {response.text}"
    except Exception as e:
        summary = f"Request failed: {str(e)}"

    st.subheader("Summary:")
    st.write(summary)

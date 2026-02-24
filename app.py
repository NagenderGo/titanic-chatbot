import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Titanic Chatbot", layout="centered")
st.title("🚢 Titanic Dataset AI Chatbot")

st.markdown("Ask questions about the Titanic dataset in plain English 👇")

@st.cache_data
def load_data():
    return pd.read_csv("data/titanic.csv")

df = load_data()

with st.expander("📊 Dataset Preview"):
    st.dataframe(df.head())

question = st.text_input("Your question:")

if question:
    with st.spinner("Thinking... 🤖"):
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        if response.status_code == 200:
            answer = response.json()["answer"]
            st.success(answer)
        else:
            st.error("❌ Failed to get response from backend")
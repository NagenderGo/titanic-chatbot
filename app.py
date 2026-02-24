import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Titanic Dataset Chatbot")

st.title("🚢 Titanic Dataset AI Chatbot")

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "titanic.csv")

df = pd.read_csv(DATA_PATH)

st.write("Ask questions about the Titanic dataset")

question = st.text_input("Your question:")

if question:
    q = question.lower()

    if "percentage" in q and "male" in q:
        pct = (df["Sex"].value_counts(normalize=True)["male"]) * 100
        st.success(f"{pct:.2f}% of passengers were male.")

    elif "average" in q and "fare" in q:
        st.success(f"Average ticket fare was {df['Fare'].mean():.2f}.")

    elif "age" in q:
        st.success(f"Average passenger age was {df['Age'].mean():.2f} years.")

    elif "embarked" in q:
        st.write(df["Embarked"].value_counts())

    else:
        st.warning("Ask about gender, fare, age, or embarkation.")

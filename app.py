import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Titanic Dataset AI Chatbot",
    page_icon="🚢",
    layout="centered"
)

st.title("🚢 Titanic Dataset AI Chatbot")
st.write("Ask questions about the Titanic dataset in plain English")

@st.cache_data
def load_data():
    return pd.read_csv("data/titanic.csv")

df = load_data()


with st.expander("📊 Dataset Preview"):
    st.dataframe(df.head())


if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Your question:")


male_words = ["male", "men", "man", "boys"]
female_words = ["female", "women", "woman", "girls"]
fare_words = ["fare", "ticket", "price", "cost"]
age_words = ["age", "old", "years"]
embark_words = ["embarked", "embark", "port", "boarding"]
survival_words = ["survived", "survival", "alive", "death"]


if question:
    q = question.lower().strip()
    answer = ""

    if any(word in q for word in male_words):
        value = (df["Sex"] == "male").mean() * 100
        answer = f"{value:.2f}% of passengers were male."

    elif any(word in q for word in female_words):
        value = (df["Sex"] == "female").mean() * 100
        answer = f"{value:.2f}% of passengers were female."

    elif any(word in q for word in fare_words):
        value = df["Fare"].mean()
        answer = f"Average ticket fare was {value:.2f}."

        fig, ax = plt.subplots()
        df["Fare"].hist(bins=30, ax=ax)
        ax.set_title("Fare Distribution")
        ax.set_xlabel("Fare")
        ax.set_ylabel("Passengers")
        st.pyplot(fig)

    elif any(word in q for word in age_words):
        value = df["Age"].mean()
        answer = f"Average age of passengers was {value:.2f} years."

        fig, ax = plt.subplots()
        df["Age"].dropna().hist(bins=30, ax=ax)
        ax.set_title("Age Distribution")
        ax.set_xlabel("Age")
        ax.set_ylabel("Passengers")
        st.pyplot(fig)

  
    elif any(word in q for word in survival_words):
        survival_rate = df["Survived"].mean() * 100
        answer = f"Overall survival rate was {survival_rate:.2f}%."

        survival_by_gender = df.groupby("Sex")["Survived"].mean() * 100

        fig, ax = plt.subplots()
        survival_by_gender.plot(kind="bar", ax=ax)
        ax.set_title("Survival Rate by Gender")
        ax.set_ylabel("Survival Percentage")
        st.pyplot(fig)
                                  
    elif any(word in q for word in embark_words):
        embark_counts = df["Embarked"].value_counts()
        answer = "Passenger embarkation counts shown below."

        fig, ax = plt.subplots()
        embark_counts.plot(kind="bar", ax=ax)
        ax.set_title("Passengers by Embarkation Port")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    else:
        answer = "Ask about gender, survival, age, fare, or embarkation."

    st.session_state.chat.append(("You", question))
    st.session_state.chat.append(("Bot", answer))


for speaker, msg in st.session_state.chat:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.success(msg)

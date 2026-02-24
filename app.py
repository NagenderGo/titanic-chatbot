import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

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


training_questions = [
    "what percentage of passengers were male",
    "how many females were there",
    "gender distribution",
    "average age of passengers",
    "how old were passengers",
    "age distribution",
    "average ticket fare",
    "ticket price",
    "fare amount",
    "how many passengers embarked from each port",
    "embarkation count",
    "ports passengers boarded from",
    "survival rate",
    "how many survived",
    "who lived"
]

training_labels = [
    "gender",
    "gender",
    "gender",
    "age",
    "age",
    "age",
    "fare",
    "fare",
    "fare",
    "embarkation",
    "embarkation",
    "embarkation",
    "survival",
    "survival",
    "survival"
]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_questions)

model = LogisticRegression()
model.fit(X_train, training_labels)


def predict_intent(question):
    X_test = vectorizer.transform([question])
    return model.predict(X_test)[0]


question = st.text_input("Your question:")


if question.strip():
    intent = predict_intent(question.lower())


    if intent == "gender":
        male_pct = (df["Sex"] == "male").mean() * 100
        female_pct = 100 - male_pct

        st.success(
            f"• Male passengers: {male_pct:.2f}%\n"
            f"• Female passengers: {female_pct:.2f}%"
        )

        fig, ax = plt.subplots()
        ax.bar(["Male", "Female"], [male_pct, female_pct])
        ax.set_ylabel("Percentage")
        ax.set_title("Gender Distribution")
        st.pyplot(fig)

    elif intent == "age":
        avg_age = df["Age"].mean()
        st.success(f"Average age of passengers was {avg_age:.2f} years.")

        fig, ax = plt.subplots()
        df["Age"].dropna().hist(ax=ax, bins=20)
        ax.set_title("Age Distribution")
        ax.set_xlabel("Age")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    elif intent == "fare":
        avg_fare = df["Fare"].mean()
        st.success(f"Average ticket fare was {avg_fare:.2f}.")

   
    elif intent == "embarkation":
        counts = df["Embarked"].value_counts()
        st.success(
            f"Passengers embarked from:\n\n"
            f"• Southampton (S): {counts.get('S', 0)}\n"
            f"• Cherbourg (C): {counts.get('C', 0)}\n"
            f"• Queenstown (Q): {counts.get('Q', 0)}"
        )

        fig, ax = plt.subplots()
        counts.plot(kind="bar", ax=ax)
        ax.set_title("Passengers by Embarkation Port")
        ax.set_xlabel("Port")
        ax.set_ylabel("Passengers")
        st.pyplot(fig)

    elif intent == "survival":
        survival_rate = df["Survived"].mean() * 100
        st.success(f"Overall survival rate was {survival_rate:.2f}%.")

    else:
        st.warning(
            "I couldn't understand the question.\n\n"
            "Try asking about:\n"
            "• gender\n"
            "• age\n"
            "• fare\n"
            "• survival\n"
            "• embarkation"
        )

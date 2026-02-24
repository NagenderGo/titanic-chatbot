from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
df = pd.read_csv("data/titanic.csv")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):
    q = data.question.lower()

    if "percentage" in q and "male" in q:
        pct = (df["Sex"].value_counts(normalize=True)["male"]) * 100
        return {"answer": f"{pct:.2f}% of passengers were male."}

    if "average" in q and "fare" in q:
        return {"answer": f"Average ticket fare was {df['Fare'].mean():.2f}."}

    if "age" in q:
        return {"answer": f"Average passenger age was {df['Age'].mean():.2f} years."}

    if "embarked" in q:
        counts = df["Embarked"].value_counts().to_dict()
        return {"answer": f"Passengers by port: {counts}"}

    return {
        "answer": "I can answer questions about gender, age, fare, and embarkation."
    }
Titanic Dataset AI Chatbot

This is a web-based chatbot that allows users to ask natural language questions
about the Titanic dataset and get instant answers.

Project Overview

This project helps users analyze the Titanic dataset by asking questions such as:
What percentage of passengers were male?
What was the average ticket fare?
How many passengers embarked from each port?

Tech Stack

Python 3.9
Streamlit for frontend
FastAPI for backend
Pandas for data analysis
Uvicorn for server

Project Structure

app.py - Streamlit frontend
api.py - FastAPI backend
data/titanic.csv - Dataset
requirements.txt - Dependencies
README.md - Documentation

How the Project Works

The user enters a question in the Streamlit app.
The question is sent to the FastAPI backend.
The backend analyzes the dataset using pandas.
The answer is returned and shown to the user.

How to Run the Project

Step 1: Create virtual environment
python -m venv venv

Step 2: Activate environment
venv\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Start backend
uvicorn api:app --reload

Step 5: Start frontend
streamlit run app.py

Example Question

What percentage of passengers were male?

Output:
64.76% of passengers were male.
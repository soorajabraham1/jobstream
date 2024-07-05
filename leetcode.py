import streamlit as st
import random

questions = []
with open('blind75.txt', 'r') as file:
    questions = [line.strip() for line in file.readlines()]

answers = []
with open('explanation.txt', 'r') as file:
    answers = [line.strip() for line in file.readlines()]
print(len(questions), len(answers))
# State variables to store the current question index
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = None

# Function to get a random question
def get_random_question():
    st.session_state.current_question_index = random.randint(0, len(questions) - 1)
    st.session_state.show_answer = False

# Function to show the answer
def show_answer():
    st.session_state.show_answer = True

# UI Elements
st.title("Quiz App")

if st.button("Next Question"):
    get_random_question()

if st.session_state.current_question_index is not None:
    st.write(f"Question: {questions[st.session_state.current_question_index]}")
    if st.button("Show Answer"):
        show_answer()

    if st.session_state.show_answer:
        st.write(f"Answer: {answers[st.session_state.current_question_index]}")
else:
    st.write("Click 'Next Question' to start the quiz.")

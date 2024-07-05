import streamlit as st
import random

# Load questions
questions = []
with open('blind75.txt', 'r') as file:
    questions = [line.strip() for line in file.readlines()]

# Load answers
answers = []
with open('explanation.txt', 'r') as file:
    answers = [line.strip() for line in file.readlines()]

# Load links
links = []
with open('link.txt', 'r') as file:
    links = [line.strip() for line in file.readlines()]

print(len(questions), len(answers), len(links))

# State variables to store the current question index
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'show_link' not in st.session_state:
    st.session_state.show_link = False

# Function to get a random question
def get_random_question():
    st.session_state.current_question_index = random.randint(0, len(questions) - 1)
    st.session_state.show_answer = False
    st.session_state.show_link = False

# UI Elements
st.title("Blind 75 Leetcode Quiz")
st.write("Welcome to the Blind 75 Leetcode Quiz! Test your knowledge with random questions from the Blind 75 list.")

st.sidebar.header("Quiz Controls")
if st.sidebar.button("Next Question", key="sidebar_next_question"):
    get_random_question()

if st.session_state.current_question_index is not None:
    st.subheader("Question:")
    st.info(questions[st.session_state.current_question_index])

    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Show Answer", key="show_answer_button"):
            st.session_state.show_answer = True
    with col2:
        if st.button("Leetcode Link", key="leetcode_link_button"):
            st.session_state.show_link = True
    with col3:
        if st.button("Next Question", key="main_next_question_button"):
            get_random_question()

    if st.session_state.show_answer:
        st.subheader("Answer:")
        st.success(answers[st.session_state.current_question_index])

    if st.session_state.show_link:
        st.subheader("Leetcode Link:")
        st.markdown(f"[Leetcode Link]({links[st.session_state.current_question_index]})", unsafe_allow_html=True)
else:
    st.write("Click 'Next Question' to start the quiz.")

import streamlit as st
import random

# Load blind75 words
blind75 = []
with open('blind75.txt', 'r') as file:
    blind75 = [line.strip() for line in file.readlines()]

# Load questions
questions = []
with open('questions.txt', 'r') as file:
    questions = [line.strip() for line in file.readlines()]

# Load companies and their URLs
companies = {}
with open('companies.txt', 'r') as file:
    companies = {line.split(" - ")[0].strip(): line.split(" - ")[1].strip() for line in file.readlines()}

# Initialize the task list and task index in session state
if 'task_index' not in st.session_state:
    st.session_state.task_index = 0
    st.session_state.tasks = ['apply', 'random_word', 'interview', 'companies', 'To DO']
    st.session_state.words = blind75
    st.session_state.questions = questions
    st.session_state.companies = companies

# Function to display the next task
def next_task():
    st.session_state.task_index = (st.session_state.task_index + 1) % len(st.session_state.tasks)

# Streamlit app layout
st.title('Task Display App')
st.write('Click the button to display the next task in order.')

# Display the current task
current_task = st.session_state.tasks[st.session_state.task_index]

if current_task == 'random_word':
    current_task = random.choice(st.session_state.words)
    st.header(current_task)

elif current_task == 'interview':
    current_task = random.choice(st.session_state.questions)
    st.header(current_task)

elif current_task == 'companies':
    current_task = random.sample(list(st.session_state.companies.keys()), 10)
    for company in current_task:
        url = st.session_state.companies[company]
        st.markdown(f"[{company}]({url})", unsafe_allow_html=True)
else:
    st.header(current_task)

# Button to go to the next task
if st.button('Next Task'):
    next_task()

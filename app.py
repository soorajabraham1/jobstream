import streamlit as st
import random


blind75 = []
with open('blind75.txt', 'r') as file:
    blind75 = [line.strip() for line in file.readlines()]

questions = []
with open('questions.txt', 'r') as file:
    questions = [line.strip() for line in file.readlines()]

companies = []
with open('companies.txt', 'r') as file:
    companies = [line.strip() for line in file.readlines()]
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
    current_task = random.choice(st.session_state.blind75) 
    
if current_task == 'interview':
    current_task = random.choice(st.session_state.questions) 

if current_task == 'companies':
    current_task = random.sample(st.session_state.companies, 10) 
    for word in current_task:
        st.header(word)
st.header(current_task)

# Button to go to the next task
if st.button('Next Task'):
    next_task()

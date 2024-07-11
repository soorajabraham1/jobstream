import streamlit as st
import tkinter as tk
from tkinter import ttk
from openai import OpenAI
from docx import Document
import docxtpl
from datetime import datetime
import io
import numpy as np
import faiss

# Mock functions and data for testing
# Replace these with your actual imports and func
def options(file_location):
    myOptions={}
    subOptions = None
    with open(file_location, "r") as file:#
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:
                continue  # Skip empty lines
            if line.endswith(":"):
                subOptions = line[:-1]  # Extract brand name (remove colon)
                myOptions[subOptions] = []  # Create an empty list for colors
            else:
                myOptions[subOptions].append(line.strip("- "))  # Add color
    return myOptions
# Load options
myOptions = options(r"textfiles\choices.txt")
def myopenai(query):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[{"role": "user", "content": query}]
    )
    return completion.choices[0].message.content

def generate(path, job_role, query,job_language):
    file_path = r'textfiles\rag\resume.txt'
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
    text = file_contents
    

    # Split document into chunks
    chunk_size = 100
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Create embeddings for each text chunk
    def get_text_embedding(input):
        client = OpenAI(api_key=api_key)
        response = client.embeddings.create(
        input= input,
        model="text-embedding-3-small"
    )
        return response.data[0].embedding


    text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])

    # Load into a vector database
    d = text_embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(text_embeddings)

    # Create embeddings for a question
    question = query
    question_embeddings = np.array([get_text_embedding(question)])

    # Retrieve similar chunks from the vector database
    D, I = index.search(question_embeddings, k=10)
    retrieved_chunk = [chunks[i] for i in I[0]]

    # Combine context and question in a prompt and generate response

    prompt = f"""
    Given the following CV and job description, generate a personalized and cohesive summary in {job_language} that retains the same idea as the CV and incorporates relevant keywords from the job description. Ensure the summary is specific, avoids generic statements, starts with "Enthusiastic {job_role} with master's and bachelor’s degree in Scientific Instrumentation, Electronics and Communication Engineering, and 1.5 years of experience in  ...", and is strictly between 45-50 words.
    CV:
    {retrieved_chunk}

    Job Description:
    {question}

    Personalized Summary  (45-50 words):
    """

    print("retrieved_chunk",retrieved_chunk)
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[ {"role": "user", "content": prompt}])

    return response.choices[0].message.content

def remove_signs(text):
    
        allowed_characters = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
        return "".join([char for char in text if char in allowed_characters])



def process_job_description(job_description_entry):
    # Extract job description from the entry field
    job_description = job_description_entry

    # Example prompt to extract information from a webpage or text
    prompt = """
    Extract the following details from the webpage/document:
    - Company name:
    - Company city:
    - Company country:
    - Job role:
    - Recruiter name (if not mentioned, set it as "Recruiter"):
    - Qualifications for the job:
    - The job post language:
    """

    input_text = job_description  # Use the job description pasted by the user
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "user", "content": prompt + input_text}]
    )

    # Extract the generated content from the response
    extracted_info = response.choices[0].message.content
    # Parse the extracted info
    lines = extracted_info.splitlines()
    return lines

# Function to parse job description

def parse_job_description(job_description):
    lines = process_job_description(job_description)
    
    company_name = ""
    company_location = ""
    company_country = ""
    job_role = ""
    recruiter_name = ""
    qualifications = ""
    job_language = ""

    for line in lines:
        if "Company name:" in line:
            company_name = line.split(":")[1].strip()
        elif "Company city:" in line:
            company_location = line.split(":")[1].strip()
        elif "Company country:" in line:
            company_country = line.split(":")[1].strip()
        elif "Job role:" in line:
            job_role = line.split(":")[1].strip()
        elif "Recruiter name:" in line:
            recruiter_name = line.split(":")[1].strip()
        elif "Qualifications for the job:" in line:
            qualifications = line.split(":")[1].strip()
        elif "The job post language:" in line:
            job_language = line.split(":")[1].strip()

    return company_name, company_location, company_country, job_role, recruiter_name, qualifications, job_language

def generate_letter(company_name, company_location, country, application_type, job_role, recruiter_name, first_point, job_first_para, job_disc_cv, job_language, doc, cv_doc):
    today_date = datetime.today().strftime("%d %B %Y")
    job_role_filtered = remove_signs(job_role)
    first_para = "write a 3 sentence starting paragraph for my cover letter showing enthusiasm in the role" + job_role + "at " + company_name + ". write in" + job_language + "language. Add things related to company to show more enthusiasm. Don't add salutation. Write in exactly 7 words. I am adding some information about the specific department in the company: "
    first_para_sentence = myopenai(first_para)

    summary_sentence = generate("path", job_first_para, job_disc_cv, job_language)

    if application_type == 'Initiative application':
        para = myOptions['Initiative application'][0]
    else:
        para = myOptions['Application'][0]

    if 'Embedded' in first_point and job_language == 'German':
        embedded_devices = myOptions['embedded_devices_german'][0]
    elif 'Embedded' in first_point and job_language == 'English':
        embedded_devices = myOptions['embedded_devices_english'][0]
    else:
        embedded_devices = ''

    if job_language == 'German':
        if first_point == 'Embedded Software Development':
            first_point = 'Entwicklung eingebetteter Software'
        elif first_point == 'Machine Learning':
            first_point = 'Maschinelles Lernen'
        elif first_point == 'Deep Learning':
            first_point = 'Deep Learning'
        elif first_point == 'Embedded Software Development and Machine Learning':
            first_point = 'Entwicklung eingebetteter Software und maschinelles Lernen'
        elif first_point == 'Software Development and Computer Vision':
            first_point = 'Softwareentwicklung und Computer Vision'
        if recruiter_name == 'Recruiter':
            recruiter_name = 'Personalvermittler'

    doc.render({'company_name': company_name,
                'company_location': company_location,
                'country': country,
                'date': today_date,
                'application_type': application_type,
                'job_role': job_role,
                'recruiter_name': recruiter_name,
                'first_point': first_point,
                'embedded_devices': embedded_devices,
                'first_para_sentence': first_para_sentence,
                'job_first_para': job_first_para,
                'company_name_short': company_name})

    cv_doc.render({'summary_sentence_english': summary_sentence,
                   'summary_sentence_german': summary_sentence})

# Streamlit app
st.title("Job Description Parser and Word Generator")
api_key = st.text_area("Password")
cv = st.file_uploader("Upload CV", type="docx")
cover = st.file_uploader("Upload Cover Letter", type="docx")

# Check if files have been uploaded
if cv and cover is not None:
    # Load the documents
    cv_doc = docxtpl.DocxTemplate(cv)
    doc = docxtpl.DocxTemplate(cover)
    
    # Display success message
    st.success("Documents uploaded successfully!")

    # Job description input
    job_description = st.text_area("Job Description")

    if st.button("Parse"):
        company_name, company_location, company_country, job_role, recruiter_name, qualifications, job_language = parse_job_description(job_description)
        st.session_state.company_name = company_name
        st.session_state.company_location = company_location
        st.session_state.company_country = company_country
        st.session_state.job_role = job_role
        st.session_state.recruiter_name = recruiter_name
        st.session_state.qualifications = qualifications
        st.session_state.job_language = job_language

    # Display parsed information
    company_name = st.text_input("Company Name", st.session_state.get('company_name', ''))
    company_location = st.text_input("Company Location", st.session_state.get('company_location', ''))
    country = st.text_input("Country", st.session_state.get('company_country', ''))
    application_type = st.selectbox("Application Type", myOptions['application_type'])
    job_role = st.text_area("Job Role", st.session_state.get('job_role', ''))
    recruiter_name = st.selectbox("Recruiter Name", myOptions['Recruiter'])
    first_point = st.selectbox("First Point", myOptions['first_point'])
    job_first_para = st.text_area("Job Role First Para", st.session_state.get('job_role', ''))
    job_qualifications = st.text_area("Job Qualifications", st.session_state.get('qualifications', ''))
    job_language = st.selectbox("Job Post Language", myOptions['company_language'])

    if st.button("Generate Word"):
        generate_letter(company_name, company_location, country, application_type, job_role, recruiter_name, first_point, job_first_para, job_qualifications, job_language, doc, cv_doc)
        st.success("Documents generated successfully!")

        # Save and provide download buttons for each document
        with io.BytesIO() as buffer1:
            doc.save(buffer1)
            buffer1.seek(0)
            st.download_button(
                label="Download Cover Letter",
                data=buffer1,
                file_name="cover_letter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        with io.BytesIO() as buffer2:
            cv_doc.save(buffer2)
            buffer2.seek(0)
            st.download_button(
                label="Download CV",
                data=buffer2,
                file_name="cv.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

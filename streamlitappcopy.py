import streamlit as st
import io
from docx import Document

# Title of the app
st.title("Upload and Download Word Document")

# File uploader
uploaded_file = st.file_uploader("Choose a Word document", type="docx")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the document
    document = Document(uploaded_file)
    
    # Display success message
    st.success("Document uploaded successfully!")

    # Download button
    with io.BytesIO() as buffer:
        document.save(buffer)
        buffer.seek(0)
        st.download_button(
            label="Download Word Document",
            data=buffer,
            file_name="downloaded_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

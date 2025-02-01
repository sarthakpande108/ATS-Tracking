from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import PyPDF2 as pdf
import json  # Import JSON module for parsing

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])

# Function to extract text from PDF
def input_pdf_text(upload_file):
    if upload_file is not None:
        reader = pdf.PdfReader(upload_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else "" 
        return text
    else:
        raise FileNotFoundError("No file uploaded")

# Function to get response from Gemini
def get_Gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()  # Remove extra spaces/newlines

# Streamlit App
st.set_page_config(page_title="ATS Resume System")
st.header("ATS Resume System")
JD = st.text_area("Job Description", "Enter the job description here:", key="input")
upload_file = st.file_uploader("Upload Resume", type=['pdf'])  

if upload_file is not None:
    st.write("PDF Uploaded Successfully") 

submit1 = st.button("Tell me About the Resume")
submit3 = st.button("What are the keywords missing in Resume")
submit4 = st.button("Percentage Match")  # New button for structured response

# Prompts
input_Prompt1 = """
You are an experienced HR with Technical Experience in the field of any one job role from Data Science, Full Stack Web Development, Generative AI, Big Data Engineering, DevOps, and Data Analysis.
Your task is to review the provided resume against the job description for these profiles. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
""" 

input_Prompt3 = """ 
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development, Generative AI, Big Data Engineering, DevOps, and Data Analysis. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as percentage, then missing keywords, and last final thoughts.
"""

# Modified prompt for JSON output
input_Prompt4 = """
Act as an advanced ATS (Applicant Tracking System) specializing in tech fields such as software engineering, data science, full-stack web development, generative AI, big data engineering, and DevOps.
Analyze the given resume and compare it with the job description. The job market is highly competitive, so provide the best possible assistance.

Return ONLY valid JSON with the following structure (NO extra text, NO markdown, NO explanations):
{
  "JD Match": "XX%", 
  "Missing keywords": ["keyword1", "keyword2"], 
  "Profile Summary": "Brief profile analysis here"
}

Resume: {text}
Job Description: {JD}
"""

# Handling button clicks
if submit1:
    if upload_file is not None:
        text = input_pdf_text(upload_file) 
        response = get_Gemini_response(input_Prompt1 + "\n\nResume:\n" + text + "\n\nJob Description:\n" + JD)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if upload_file is not None:
        pdf_content = input_pdf_text(upload_file)
        response = get_Gemini_response(input_Prompt3 + "\n\nResume:\n" + pdf_content + "\n\nJob Description:\n" + JD)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:  # Structured ATS response
    if upload_file is not None:
        pdf_content = input_pdf_text(upload_file)
        structured_prompt = input_Prompt4.replace("{text}", pdf_content).replace("{JD}", JD)
        raw_response = get_Gemini_response(structured_prompt)

        # Try to parse JSON safely
        try:
            parsed_response = json.loads(raw_response)  # Convert response to JSON
            st.subheader("ATS Analysis (Structured Response):")
            st.json(parsed_response)  # Display properly formatted JSON
        except json.JSONDecodeError:
            st.error("Failed to parse response as JSON. Raw response:")
            st.text(raw_response)  # Show raw response in case of error
    else:
        st.write("Please upload the resume")

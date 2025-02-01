from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import base64
import  google.generativeai as genai
import io
import PyPDF2 as pdf


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
def get_Gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input)
    return response.text



def input_pdf_text(upload_file):
    if upload_file is not None:
        reader = pdf.PdfReader(upload_file)
        text = ""
        for page in reader(len(reader.pages)):
            page=reader.pages[page]
            text += str(page.extract_text())  # Extract text from each page
        
        return text
    else:
        raise FileNotFoundError("No file uploaded")

    
#Streamlit App
st.set_page_config(page_title="ATS Resume System")
st.header("Ats Resume System")
JD=st.text_area("Job Discrption","Enter the job description here:",key="input")
upload_file=st.file_uploader("Upload Resume",type=['pdf'])  

if upload_file is not None:
        st.write("Pdf Uploaded Successfully") 
submit1=st.button("Tell me About the resume")
submit2=st.button("How Can I improve my resume")
submit3=st.button("What are the keywords missing in resume")
submit4 =st.button("Percentage match")

input_Prompt1="""
 You are an experienced HR with Technical Experience in the field of  any one job role from Data Science or Full stack web development,Generative AI,Big Data Engineering,DevOPS  and Data Analysis ,
 your task is to review the provided resume against the job description for this profiles. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
""" 

 
input_Prompt3=""" 
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role data science,,Full stack web development,Generative AI,Big Data Engineering,DevOPS , Data Analysis  and  deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_Prompt4="""
Hey Act like a skilled or very experience ATS(Applicant Tracking System)
with a deep understanding of tech field, software engineering, data science, full stack web development, generative AI, big data engineering, DevOps, and data analysis.
your task is to evaluate the resume based on given job description.
you must consider the job market is very competitive and you should provide best assistance for improving the resume.
Assign the percentage matching based on job description and the missing keywords with high accuracy.
resume:{text}
description:{JD}

I want the responsee in single string having the following structure
{{"JD Match":"%","Misssing keywords":"[]","Profile Summary":""}}
"""

if submit1:
    if upload_file is not None:
        text=input_pdf_setup(upload_file) 
        response=get_Gemini_response(input_Prompt1,text,JD)
        st.subheader("the responses is")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit3:
        if upload_file is not None:
            pdf_content=input_pdf_setup(upload_file)
            response=get_Gemini_response(input_Prompt3,pdf_content,input_text)
            st.subheader("the responses is")
            st.write(response)
        else:
            st.write("Please upload the resume")
    





        
 
    
    
    

    
    
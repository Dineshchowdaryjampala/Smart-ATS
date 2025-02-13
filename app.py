import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# Prompt Templates
input_prompt_1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and 
weaknesses of the applicant in relation to the specified job requirements.
resume:{text}
description:{jd}
"""

input_prompt_3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give the percentage of match if the resume matches 
the job description. First, the output should come as percentage and then keywords missing, and last final thoughts.
resume:{text}
description:{jd}
"""

input_prompt_summary = """
Hey, act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, 
software engineering, data science, data analytics, and big data engineering. Your task is to evaluate the resume based on 
the given job description. You must consider that the job market is very competitive, and you should provide the best 
assistance for improving the resumes. Assign the percentage matching based on the job description and the missing keywords 
with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%", "MissingKeywords":[], "Profile Summary":""}}
"""

# Streamlit App
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")

# User Inputs
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF file")

# Buttons
submit_review = st.button("Tell Me About the Resume")
submit_match = st.button("Percentage Match")
submit_summary = st.button("Submit")

# Process Resume Review
if submit_review:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt = input_prompt_1.format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Process Percentage Match
if submit_match:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt = input_prompt_3.format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Process Summary with structured output
if submit_summary:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        if jd and text:
            prompt = input_prompt_summary.format(text=text, jd=jd)
            response = get_gemini_response(prompt)

            # Format the response for better readability
            try:
                response_dict = json.loads(response)
                st.subheader("The Response is:")
                st.write(f"**JD Match:** {response_dict.get('JD Match', 'N/A')}")
                st.write(f"**Missing Keywords:** {', '.join(response_dict.get('MissingKeywords', []))}")
                st.write(f"**Profile Summary:** {response_dict.get('Profile Summary', 'N/A')}")
            except json.JSONDecodeError:
                st.write("Error: Unable to parse response. Please check the response format.")
        else:
            st.write("Error: Please ensure both the job description and resume are provided.")
    else:
        st.write("Please upload the resume.")

# Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            color: #333;
        }
    </style>
    <div class="footer">
        Developed by <a href="https://github.com/Dineshchowdaryjampala" target="_blank">J DINESH CHOWDARY</a>
    </div>
    """,
    unsafe_allow_html=True
)

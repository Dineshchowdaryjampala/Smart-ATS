# Smart ATS - Resume Analyzer

Smart ATS is an AI-powered resume analyzer that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). The application compares a resume against a given job description and provides insights, such as match percentage, missing keywords, and an overall profile summary.

## 🚀 Features
- 📄 **Resume Review**: Get a detailed evaluation of your resume against a job description.
- 📊 **Percentage Match**: Find out how well your resume aligns with the job description.
- 🔍 **Missing Keywords**: Identify important keywords missing in your resume.
- 📝 **Profile Summary**: Receive AI-generated feedback for improvement.
- 📂 **PDF Resume Support**: Upload your resume in PDF format.

## 🛠️ Tech Stack
- **Python** 🐍
- **Streamlit** 🎨 (For Web UI)
- **Google Gemini AI** 🤖 (For resume analysis)
- **PyPDF2** 📄 (For extracting text from PDFs)
- **dotenv** 🔑 (For environment variable management)

## 📦 Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/Dineshchowdaryjampala/Smart-ATS.git
   cd Smart-ATS
   ```

2. **Create a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up API key**
   - Create a `.env` file in the project directory
   - Add your Google API key:
     ```sh
     GOOGLE_API_KEY=your_google_gemini_api_key
     ```

5. **Run the application**
   ```sh
   streamlit run app.py
   ```

## 📌 Usage
1. Paste the job description in the text area.
2. Upload your resume (PDF format only).
3. Click on **"Tell Me About the Resume"** for a detailed review.
4. Click on **"Percentage Match"** to check resume-job description alignment.
5. Click on **"Submit"** to receive ATS recommendations.

## 📷 Screenshots

## 🏆 Author
Developed by **[J Dinesh Chowdary](https://github.com/Dineshchowdaryjampala)** 🚀

## 📝 License
This project is **open-source** and available under the [MIT License](LICENSE). Feel free to contribute! 😊


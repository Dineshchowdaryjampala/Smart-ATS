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
# Home_Page
![gb](https://github.com/Dineshchowdaryjampala/Smart-ATS/blob/f5f5b5866e1e3796f2a5bc9c5599ae8178d08497/Images/Home_Page.png)
# Percentage_Match
![gb](https://github.com/Dineshchowdaryjampala/Smart-ATS/blob/f5f5b5866e1e3796f2a5bc9c5599ae8178d08497/Images/Percentage_Match.png)
# Tell_Me_About_Resume
![gb](https://github.com/Dineshchowdaryjampala/Smart-ATS/blob/f5f5b5866e1e3796f2a5bc9c5599ae8178d08497/Images/Tell_me_about_resume%20.png)
## 🏆 Author
Developed by **[J Dinesh Chowdary](https://github.com/Dineshchowdaryjampala)** 🚀

## 📝 License
This project is **open-source** and available under the [MIT License](LICENSE). Feel free to contribute! 😊
## 📢 Contributing
Feel free to **fork** this repository, create a **new branch**, and submit a **pull request**!

## 📬 Contact
📧 Email: dineshwalker143@gmail.com
🔗 GitHub: [Your Profile](https://github.com/Dineshchowdaryjampala)

🚀 **Star this repository** if you find it useful! Happy Coding! 😊

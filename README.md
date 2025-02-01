# 🚀 ATS Resume System

![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

## 📌 Overview

ATS Resume System is a **Streamlit-based web app** that analyzes resumes against job descriptions using **Google Gemini AI**. It provides **resume insights, missing keywords, and ATS match percentages** to help candidates optimize their resumes.

## ✨ Features

- 📄 **Upload Resume (PDF format)**
- 🎯 **Analyze resume against job description**
- 🔍 **Identify missing keywords**
- 📊 **Calculate ATS match percentage**
- 💡 **Suggest improvements**

## 🏗️ Tech Stack

- **Python** 🐍
- **Streamlit** 🎨 (Frontend framework)
- **Google Gemini AI** 🤖 (LLM-based analysis)
- **PyPDF2** 📜 (PDF text extraction)
- **pdf2image** 📷 (PDF to image conversion, if needed)
- **dotenv** 🔐 (For API key management)

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sarthakpande108/ATS-Tracking.git
cd ATS-Tracking
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key

Create a `.env` file in the root directory and add your **Google Gemini API key**:

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

## 🌍 Deployment (Free Hosting)

You can deploy this project for free using **Streamlit Community Cloud**.

### Steps to Deploy:

1. Push your project to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in.
3. Click **New App** → Select your **GitHub repository**.
4. Set `app.py` as the main file.
5. Click **Deploy** and get your live URL!

## 📸 Screenshots

*Include screenshots of your application here*

## 🛠️ How It Works

1. Upload your **resume (PDF format)**.
2. Enter a **job description**.
3. Click on one of the analysis buttons:
   - **Tell me about the resume** → Gives strengths & weaknesses.
   - **How can I improve my resume?** → Provides suggestions.
   - **What are the keywords missing?** → Shows missing ATS keywords.
   - **Percentage match** → Calculates ATS match %.
4. View AI-generated feedback.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request. 🎯

## 📜 License

This project is licensed under the **MIT License**.

## 👤 Author

- **Sarthak Pande** 👨‍💻
- LinkedIn: [Sarthak Pande](https://www.linkedin.com/in/sarthak-pande-1435a1229/)
- GitHub: [Sarthak Pande](https://github.com/sarthakpande108)

---

💡 *Improve your resume and land your dream job with AI-powered insights!* 🚀


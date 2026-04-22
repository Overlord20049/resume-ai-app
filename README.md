# 🚀 AI Resume Matcher

A web-based application that analyzes resumes and compares them with job descriptions using NLP techniques.

## 🔥 Features

- Upload resume (PDF)
- Paste job description
- Calculates match score using cosine similarity
- Displays:
  - ✅ Skills found
  - ❌ Missing skills
- Clean UI with interactive results

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- PyPDF2
- HTML/CSS

## 📊 How It Works

1. Extracts text from resume PDF  
2. Converts resume + job description into vectors  
3. Computes similarity using cosine similarity  
4. Identifies matching and missing skills  

## ▶️ Run Locally

```bash
pip install flask scikit-learn PyPDF2
python3 app.py

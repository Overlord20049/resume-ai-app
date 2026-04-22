from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Skill database
SKILLS_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "sql", "mongodb", "flask", "django", "react",
    "html", "css", "javascript", "data analysis"
]

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def match_score(resume_text, job_text):
    texts = [resume_text, job_text]
    cv = CountVectorizer()
    matrix = cv.fit_transform(texts)
    score = cosine_similarity(matrix)[0][1]
    return round(score * 100, 2)

def extract_skills(text):
    found = []
    for skill in SKILLS_DB:
        if skill in text:
            found.append(skill)
    return found

from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def match_score(resume_text, job_text):
    # --- similarity score ---
    texts = [resume_text, job_text]
    cv = CountVectorizer()
    matrix = cv.fit_transform(texts)
    score = cosine_similarity(matrix)[0][1]

    # --- skills list ---
    skills = [
        "python", "sql", "machine learning", "api",
        "data analysis", "java", "c++", "html", "css",
        "javascript", "react", "node", "mongodb"
    ]

    resume_lower = resume_text.lower()
    job_lower = job_text.lower()

    found = []
    missing = []

    for skill in skills:
        if skill in resume_lower:
            found.append(skill)

        if skill in job_lower and skill not in resume_lower:
            missing.append(skill)

    return round(score * 100, 2), found, missing

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
    texts = [resume_text, job_text]
    cv = CountVectorizer()
    matrix = cv.fit_transform(texts)
    score = cosine_similarity(matrix)[0][1]
    return round(score * 100, 2)

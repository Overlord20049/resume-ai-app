from flask import Flask, render_template, request
from utils import extract_text, match_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    matched = []
    missing = []

    if request.method == "POST":
        file = request.files.get("resume")
        job_desc = request.form.get("job_description")

        if file and job_desc:
            resume_text = extract_text(file).lower()
            job_words = job_desc.lower().split()

            score = match_score(resume_text, job_desc)

            matched = [word for word in job_words if word in resume_text]
            missing = [word for word in job_words if word not in resume_text]

            matched = list(set(matched))[:5]
            missing = list(set(missing))[:5]

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing
    )


@app.route("/test")
def test():
    return "WORKING 🚀"


# REQUIRED for gunicorn
app = app

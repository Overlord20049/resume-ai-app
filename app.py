from flask import Flask, render_template, request
from utils import extract_text, match_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []

    if request.method == "POST":
        file = request.files.get("resume")
        job_desc = request.form.get("job_description")

        if file and job_desc:
            resume_text = extract_text(file)
            score = match_score(resume_text, job_desc)
            skills = job_desc.lower().split()[:5]

    return render_template("index.html", score=score, skills=skills)


# ✅ TEST ROUTE
@app.route("/test")
def test():
    return "Working 🚀"


# ✅ THIS LINE IS CRITICAL FOR RENDER
app = app

from flask import Flask, render_template, request
from utils import extract_text, match_score, extract_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_description"]

        resume_text = extract_text(file)
        score = match_score(resume_text, job_desc)
        skills = extract_skills(resume_text)

    return render_template("index.html", score=score, skills=skills)

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

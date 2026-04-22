from flask import Flask, render_template, request
from utils import extract_text, match_score

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    found = []
    missing = []

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        if file:
            resume_text = extract_text(file)
            score, found, missing = match_score(resume_text, job_desc)

    return render_template("index.html", score=score, found=found, missing=missing)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

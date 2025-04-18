from flask import Flask, request, render_template
from summarizer import TextSummarizer

app = Flask(__name__)
summarizer = TextSummarizer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        summary = summarizer.summarize(text)
        return render_template("index.html", summary=summary, original=text)
    return render_template("index.html", summary=None)

if __name__ == "__main__":
    app.run(debug=True)


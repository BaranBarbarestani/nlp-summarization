from flask import Flask, request, render_template
from summarizer import TextSummarizer

app = Flask(__name__)
summarizer = TextSummarizer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the text entered by the user
        text = request.form["text"]
        # Generate the summary using the TextSummarizer
        summary = summarizer.summarize(text)
        # Render the template with both original text and its summary
        return render_template("index.html", summary=summary, original=text)
    return render_template("index.html", summary=None)

if __name__ == "__main__":
    app.run(debug=True)

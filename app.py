from flask import Flask, render_template, request, redirect
from src.chatbot import get_response
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    answer = None
    intent = None
    confidence = None
    entities = []
    question = ""

    if request.method == "POST":

        question = request.form["question"]

        if question.strip():

            intent, confidence, answer, entities = get_response(question)

    return render_template(
        "index.html",
        question=question,
        answer=answer,
        intent=intent,
        confidence=confidence,
        entities=entities
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        question = request.form["question"]
        intent = request.form["intent"]
        answer = request.form["answer"]

        new_data = pd.DataFrame([{
            "question": question,
            "intent": intent,
            "answer": answer
        }])

        new_data.to_csv(
            "data/faq_dataset.csv",
            mode="a",
            header=False,
            index=False
        )

        return redirect("/admin")

    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
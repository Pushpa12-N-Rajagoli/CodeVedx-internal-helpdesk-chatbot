from flask import Flask, render_template, request, session, redirect
from src.chatbot import get_response

app = Flask(__name__)

# Secret key for storing chat history
app.secret_key = "internal_helpdesk_chatbot_key"


@app.route("/", methods=["GET", "POST"])
def home():

    # Create chat history if it does not exist
    if "messages" not in session:
        session["messages"] = []

    # When user sends a question
    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if question:

            # Get chatbot response
            intent, confidence, answer, entities = get_response(question)

            # Add question and answer to chat history
            session["messages"].append({
                "question": question,
                "answer": answer
            })

            session.modified = True

    return render_template(
        "index.html",
        messages=session["messages"]
    )


@app.route("/clear")
def clear_chat():

    # Remove previous conversation
    session.pop("messages", None)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
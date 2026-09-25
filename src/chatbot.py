import joblib
import pandas as pd
from pathlib import Path

from src.preprocess import clean_text


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Load trained model
model = joblib.load(
    BASE_DIR / "models" / "chatbot_model.pkl"
)

# Load TF-IDF vectorizer
vectorizer = joblib.load(
    BASE_DIR / "models" / "tfidf_vectorizer.pkl"
)

# Load FAQ dataset
faq_data = pd.read_csv(
    BASE_DIR / "data" / "faq_dataset.csv"
)


# Entity recognition
def extract_entities(question):

    question_lower = question.lower()

    entities = []

    if "hr" in question_lower:
        entities.append("HR")

    if "it" in question_lower or "technical" in question_lower:
        entities.append("IT")

    if "leave" in question_lower:
        entities.append("Leave")

    if "salary" in question_lower:
        entities.append("Salary")

    if "attendance" in question_lower:
        entities.append("Attendance")

    if "password" in question_lower:
        entities.append("Password")

    return entities


# Chatbot response
def get_response(question):

    # Clean question
    cleaned_question = clean_text(question)

    # Convert question into TF-IDF
    question_vector = vectorizer.transform(
        [cleaned_question]
    )

    # Predict intent
    intent = model.predict(question_vector)[0]

    # Confidence
    probabilities = model.predict_proba(question_vector)[0]

    confidence = max(probabilities) * 100


    # Keyword-based correction
    question_lower = question.lower()

    if "it support" in question_lower:
        intent = "it_support"

    elif "technical support" in question_lower:
        intent = "it_support"

    elif "password" in question_lower:
        intent = "password_reset"

    elif "leave" in question_lower:
        intent = "leave_policy"

    elif "salary" in question_lower:
        intent = "salary"

    elif "attendance" in question_lower:
        intent = "attendance"

    elif "hr" in question_lower:
        intent = "hr_contact"

    elif "office address" in question_lower:
        intent = "office_location"

    elif "office location" in question_lower:
        intent = "office_location"

    elif "working hours" in question_lower:
        intent = "working_hours"

    elif "office timings" in question_lower:
        intent = "working_hours"


    # Find answer
    matching_rows = faq_data[
        faq_data["intent"] == intent
    ]


    if not matching_rows.empty:

        answer = matching_rows.iloc[0]["answer"]

    else:

        answer = (
            "Sorry, I could not find an answer "
            "to your question."
        )


    # Extract entities
    entities = extract_entities(question)


    return intent, confidence, answer, entities
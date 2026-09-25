# AI Internal Helpdesk Chatbot

An AI-powered internal helpdesk chatbot built using Python, NLP, Machine Learning, and Flask. The chatbot helps employees get quick answers to common workplace questions related to HR, leave, salary, attendance, password reset, IT support, and office information.

## Features

- FAQ-based question-answer chatbot
- NLP text preprocessing
- Intent detection
- Basic entity recognition
- FAQ dataset preparation
- TF-IDF text vectorization
- Logistic Regression machine learning model
- Confidence score
- Flask web application
- Admin panel for adding new FAQs
- Simple and user-friendly web interface

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TF-IDF
- Logistic Regression
- Joblib
- HTML
- CSS
- Git & GitHub

## Project Structure

```text
internal_helpdesk_chatbot/
│
├── data/
│   └── faq_dataset.csv
│
├── models/
│   ├── chatbot_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── chatbot.py
│
├── templates/
│   ├── index.html
│   └── admin.html
│
├── static/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

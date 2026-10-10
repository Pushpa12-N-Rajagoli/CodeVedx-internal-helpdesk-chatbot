# 🤖 AI Internal Helpdesk Chatbot

An AI-powered internal helpdesk chatbot developed using Python, Natural Language Processing (NLP), and Machine Learning.

The chatbot helps employees get quick answers to common workplace-related questions such as HR, leave, salary, attendance, IT support, password reset, and office information.

---

## 📌 Project Overview

The AI Internal Helpdesk Chatbot is designed to provide automated support for common employee queries.

Instead of manually contacting HR or IT for basic questions, employees can interact with the chatbot through a simple web interface and receive relevant responses instantly.

The system uses **TF-IDF vectorization** and **Machine Learning classification** to understand the user's question and identify the appropriate intent.

---

## ✨ Features

- AI-powered employee support chatbot
- Interactive chat-style web interface
- NLP-based text processing
- TF-IDF feature extraction
- Machine Learning-based intent classification
- Password reset assistance
- Leave-related information
- Salary and payroll support
- HR contact information
- Working hours information
- Attendance support
- IT and technical support
- Office location information
- Clear conversation option
- Responsive web interface

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- NLTK
- TF-IDF
- Logistic Regression
- Joblib
- HTML
- CSS

---

## 🧠 Machine Learning Approach

The chatbot follows these steps:

1. User enters a question.
2. The question is cleaned using NLP preprocessing.
3. The cleaned text is converted into numerical features using **TF-IDF**.
4. The trained Machine Learning model predicts the user's intent.
5. The chatbot searches the FAQ dataset for the corresponding answer.
6. The answer is displayed in the chat interface.

## Project structure
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
│   ├── chatbot.py
│   ├── preprocess.py
│   └── train_model.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md



### Example

```text
User:
How can I reset my password?

Chatbot:
You can reset your password using the password reset
option on the employee portal. If you still cannot
access your account, please contact IT support.



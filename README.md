# 🎓 Student Performance Prediction System

A full-stack **Machine Learning Web Application** that predicts student math performance and provides interactive analytics through a dashboard.

---

## 📌 Project Overview

This project combines **Machine Learning, Flask, and Data Visualization** to:

- Predict student math scores using a trained ML model  
- Store predictions in a database  
- Visualize results through interactive charts  
- Provide intelligent performance insights  

---

## 🚀 Features

### 🧠 Prediction System
- Predicts math score using ML model  
- Input features include:
  - Gender  
  - Reading Score  
  - Writing Score  
  - Parental Education  
  - Lunch Type  
  - Test Preparation Course  

---

### 📊 Analytics Dashboard
- 📈 Prediction Trend (Line Chart)  
- 📊 Score Distribution (Histogram)  
- 🥧 Performance Breakdown (Pie Chart)  
- 📋 Prediction History Table  

---

### 🧠 AI Insights
- Excellent Performance 🎉  
- Average Performance 👍  
- Needs Improvement ⚠️  

---

### 🗑 Data Management
- Stores predictions in SQLite database  
- Clear entire history with one click  

---

## 🛠 Tech Stack

| Category | Tools |
|----------|------|
| Backend | Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Chart.js |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite |

---

## 📁 Project Structure

```bash
mlproject/
│
├── app/                         # Flask application
│   ├── __init__.py              # App factory
│   ├── routes.py                # All routes
│   └── db.py                    # Database logic
│
├── templates/                   # HTML templates
│   ├── index.html
│   ├── predict.html
│   └── dashboard.html
│
├── static/                      # Static files (CSS, JS)
│
├── src/                         # ML pipeline
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── artifacts/                   # Saved models
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── data/                        # Dataset
│   └── data.csv
│
├── notebooks/                   # Jupyter notebooks
│
├── config/                      # Config files
│
├── run.py                       # Entry point
├── students.db                  # SQLite DB
├── requirements.txt
└── README.md
from flask import Flask, request, render_template, redirect
import pandas as pd
import sqlite3
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# -------------------------
# DATABASE SETUP
# -------------------------
def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            reading_score REAL,
            writing_score REAL,
            prediction REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -------------------------
# ROUTES
# -------------------------

# 🏠 Home
@app.route('/')
def index():
    return render_template('index.html')


# 🧠 Prediction
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    
    try:
        # -------------------------
        # SAFE INPUT HANDLING
        # -------------------------
        gender = request.form.get('gender') or 'male'
        ethnicity = request.form.get('ethnicity') or 'group C'
        parental = request.form.get('parental_level_of_education') or 'some college'
        lunch = request.form.get('lunch') or 'standard'
        course = request.form.get('test_preparation_course') or 'none'

        reading = float(request.form.get('reading_score') or 0)
        writing = float(request.form.get('writing_score') or 0)

        # -------------------------
        # CREATE DATA OBJECT
        # -------------------------
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental,
            lunch=lunch,
            test_preparation_course=course,
            reading_score=reading,
            writing_score=writing
        )

        pred_df = data.get_data_as_data_frame()

        # -------------------------
        # PREDICTION
        # -------------------------
        predict_pipeline = PredictPipeline()
        result = round(predict_pipeline.predict(pred_df)[0], 2)

        # -------------------------
        # PERFORMANCE MESSAGE
        # -------------------------
        if result > 75:
            message = "Excellent Performance 🎉"
        elif result > 50:
            message = "Average Performance 👍"
        else:
            message = "Needs Improvement ⚠️"

        # -------------------------
        # SAVE TO DATABASE
        # -------------------------
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO predictions (gender, reading_score, writing_score, prediction) VALUES (?, ?, ?, ?)",
            (gender, reading, writing, result)
        )
        conn.commit()
        conn.close()

        return render_template('predict.html', result=result, message=message)

    except Exception as e:
        return render_template('predict.html', error=str(e))


# 📊 Dashboard
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('students.db')
    df = pd.read_sql_query("SELECT * FROM predictions", conn)
    conn.close()

    # -------------------------
    # ANALYTICS
    # -------------------------
    avg_score = round(df['prediction'].mean(), 2) if not df.empty else 0
    max_score = round(df['prediction'].max(), 2) if not df.empty else 0
    min_score = round(df['prediction'].min(), 2) if not df.empty else 0

    # -------------------------
    # AI INSIGHT
    # -------------------------
    if df.empty:
        insight = "No data available yet ⚠️"
    elif avg_score > 75:
        insight = "Overall performance is excellent 🎉"
    elif avg_score > 50:
        insight = "Students are performing average 👍"
    else:
        insight = "Performance needs improvement ⚠️"

    return render_template(
        'dashboard.html',
        tables=df.to_dict(orient='records'),
        avg_score=avg_score,
        max_score=max_score,
        min_score=min_score,
        insight=insight
    )


# 🗑 CLEAR HISTORY (NEW FEATURE)
@app.route('/clear')
def clear_history():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("DELETE FROM predictions")
    conn.commit()
    conn.close()

    return redirect('/dashboard')


# -------------------------
# RUN APP
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_productivity_model.pkl")

st.title("🎓 Student Productivity Predictor")

st.write("Enter the student's details to predict the productivity score.")

age = st.number_input("Age", 15, 50, 20)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

study_hours = st.number_input(
    "Study Hours Per Day", 0.0, 24.0, 5.0
)

sleep_hours = st.number_input(
    "Sleep Hours", 0.0, 24.0, 7.0
)

phone_usage = st.number_input(
    "Phone Usage Hours", 0.0, 24.0, 2.0
)

social_media = st.number_input(
    "Social Media Hours", 0.0, 24.0, 2.0
)

youtube = st.number_input(
    "YouTube Hours", 0.0, 24.0, 1.0
)

gaming = st.number_input(
    "Gaming Hours", 0.0, 24.0, 1.0
)

breaks = st.number_input(
    "Breaks Per Day", 0, 20, 3
)

coffee = st.number_input(
    "Coffee Intake (mg)", 0, 1000, 100
)

exercise = st.number_input(
    "Exercise Minutes", 0, 300, 30
)

assignments = st.number_input(
    "Assignments Completed", 0, 100, 5
)

attendance = st.number_input(
    "Attendance Percentage", 0.0, 100.0, 75.0
)

stress = st.number_input(
    "Stress Level", 0.0, 10.0, 5.0
)

focus = st.number_input(
    "Focus Score", 0.0, 10.0, 5.0
)

final_grade = st.number_input(
    "Final Grade", 0.0, 100.0, 70.0
)

if st.button("Predict Productivity"):

    input_data = pd.DataFrame({
        "AGE": [age],
        "GENDER": [gender],
        "STUDY_HOURS_PER_DAY": [study_hours],
        "SLEEP_HOURS": [sleep_hours],
        "PHONE_USAGE_HOURS": [phone_usage],
        "SOCIAL_MEDIA_HOURS": [social_media],
        "YOUTUBE_HOURS": [youtube],
        "GAMING_HOURS": [gaming],
        "BREAKS_PER_DAY": [breaks],
        "COFFEE_INTAKE_MG": [coffee],
        "EXERCISE_MINUTES": [exercise],
        "ASSIGNMENTS_COMPLETED": [assignments],
        "ATTENDANCE_PERCENTAGE": [attendance],
        "STRESS_LEVEL": [stress],
        "FOCUS_SCORE": [focus],
        "FINAL_GRADE": [final_grade]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Productivity Score: {prediction:.2f}"
    )

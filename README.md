# EduPredict AI - Student Dropout & Academic Success Prediction 🚀🎓

An End-to-End Machine Learning and interactive Streamlit web application designed to predict the academic outcome of students. By analyzing historical, demographic, and academic data, the model classifies students into three categories: **Dropout**, **Enrolled**, or **Graduate**. This helps educational institutions take timely actions to support struggling students.

## 🎯 Objective & Problem Statement
Student dropout and academic progression are critical challenges in educational institutions. The goal of this project is to build a multi-class classification model that can predict a student's academic future early on, allowing teachers and management to step in with targeted interventions.

## 🛠️ Tech Stack & Workflow
- **Language:** Python
- **Data Analytics:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Web App Frontend:** Streamlit (Custom Premium CSS UI)
- **Model Serialization:** Joblib (`student_model.pkl`)

## 📊 Dataset Features & Parameters
The dataset contains comprehensive information about students, including:
- **Demographic Data:** Marital status, Nationality, Gender, Age at enrollment.
- **Socio-economic Data:** Income, Tuition fees status, Scholarship holder, Parents' qualification & occupation.
- **Academic Performance (1st & 2nd Semester):** Curricular units credited, enrolled, evaluations, approved, and grades.
- **Target Variable:** `Dropout`, `Enrolled`, `Graduate`.

## 📈 Key Insights & Machine Learning Results
- **Data Preprocessing:** Cleaned the raw student logs, handled target mapping, and split the data into training and testing sets.
- **Model Used:** Built a **Random Forest Classifier** which handles the multi-class target variable smoothly.
- **Performance Evaluation:** Achieved an overall accuracy of **78%**. The classification report shows excellent precision and recall metrics, especially for predicting graduates and dropouts.
- **Actionable Insights:** The app includes a unique feature that provides proactive recommendations for teachers based on the predicted status (e.g., offering extra tutorial classes or 1-on-1 counseling for high-risk profiles).

## 📂 Project Structure
- `data.csv` - The primary historical dataset containing student features.
- `students_dropout_rate.ipynb` - Jupyter Notebook covering complete EDA, data modeling, and model training.
- `app.py` - Premium-themed Streamlit application backend and interface.
- `student_model.pkl` - The trained Random Forest model file.
- `README.md` - Comprehensive documentation.

## 💻 How to Run This Project Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/student-dropout-rate-prediction.git](https://github.com/YOUR_USERNAME/student-dropout-rate-prediction.git)

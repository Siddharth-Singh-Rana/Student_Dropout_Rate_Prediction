import streamlit as st
import pandas as pd
import joblib
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="EduPredict AI", layout="wide", page_icon="🚀", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
    <style>
    /* Main Background & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Gradient Predict Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        font-weight: bold;
        font-size: 22px;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0px 8px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease 0s;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        box-shadow: 0px 15px 20px rgba(0,0,0,0.4);
        transform: translateY(-3px);
    }
    
    /* Custom Headers */
    h1, h2, h3 { color: #1e3c72; }
    
    /* Divider Customization */
    hr { border-top: 2px dashed #d1d5db; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAV ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135810.png", width=100)
    st.title("🚀 EduPredict AI")
    st.caption("v2.0 Premium Edition")
    st.markdown("---")
    st.markdown("### 💡 Quick Guide:")
    st.info("1. Enter details in the right panel.\n2. Verify the Academic & Economic sections.\n3. Hit the **Predict** button below to see the magic.")
    st.markdown("---")
    st.write("Developed with ❤️ using ML")

# --- HEADER WITH BANNER ---
# Ek premium banner image (Unsplash se)
st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2000&auto=format&fit=crop", use_container_width=True)

st.title("🎓 Student Academic Outcome Predictor")
st.markdown("Is AI Dashboard ki madad se student ki profile ko analyze karein aur uske **Dropout**, **Enrollment**, ya **Graduation** hone ki sambhavna ko pehle se jaaniyo.")
st.markdown("---")

# --- MAPPINGS ---
marital_mapping = {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto Union", 6: "Legally Separated"}
yes_no_mapping = {0: "No", 1: "Yes"}
gender_mapping = {0: "Female", 1: "Male"}
attendance_mapping = {0: "Evening", 1: "Daytime"}

qual_mapping = {1: "Secondary (12th)", 2: "Bachelor's", 3: "Degree", 4: "Master's", 5: "Doctorate", 19: "Basic Education", 37: "Unknown", 38: "Illiterate"}
occ_mapping = {0: "Student", 1: "Management", 2: "Admin", 3: "Sales/Service", 4: "Agriculture", 5: "Industry", 9: "Unskilled", 10: "Other"}

course_options = [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991]

# --- MAIN TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🧑‍🎓 Profile", "📚 Academics", "📊 Grades", "🌍 Economy"])

with tab1:
    st.subheader("Personal details")
    col1, col2, col3 = st.columns(3)
    marital_status = col1.selectbox("Marital status", options=list(marital_mapping.keys()), format_func=lambda x: marital_mapping[x])
    gender = col2.selectbox("Gender", options=list(gender_mapping.keys()), format_func=lambda x: gender_mapping[x])
    age = col3.number_input("Age at enrollment", min_value=15, value=20)

    st.subheader("Family Background")
    col_m, col_f = st.columns(2)
    m_qual = col_m.selectbox("Mother's Qualification", options=list(qual_mapping.keys()), format_func=lambda x: qual_mapping[x])
    m_occ = col_m.selectbox("Mother's Occupation", options=list(occ_mapping.keys()), format_func=lambda x: occ_mapping[x])
    f_qual = col_f.selectbox("Father's Qualification", options=list(qual_mapping.keys()), format_func=lambda x: qual_mapping[x])
    f_occ = col_f.selectbox("Father's Occupation", options=list(occ_mapping.keys()), format_func=lambda x: occ_mapping[x])

with tab2:
    st.subheader("Course & Finance")
    col1, col2, col3 = st.columns(3)
    course = col1.selectbox("Course Enrolled", options=course_options, format_func=lambda x: f"Course Code: {x}")
    attendance = col2.selectbox("Attendance Type", options=list(attendance_mapping.keys()), format_func=lambda x: attendance_mapping[x])
    scholarship = col3.selectbox("Has Scholarship?", options=list(yes_no_mapping.keys()), format_func=lambda x: yes_no_mapping[x])
    
    admission_grade = st.slider("Admission Grade (0 - 200)", 0.0, 200.0, 130.0)
    prev_qual_grade = st.slider("Previous Qualification Grade (0 - 200)", 0.0, 200.0, 130.0)
    
    app_mode = 1; app_order = 1; prev_qual = 1; nationality = 1; displaced = 0; special_needs = 0; debtor = 0; tuition_up_to_date = 1; international = 0

with tab3:
    st.subheader("Semester-wise Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Semester 1 Data**")
        s1_enrolled = st.number_input("Enrolled Units (S1)", value=6)
        s1_approved = st.number_input("Approved Units (S1)", value=6)
        s1_grade = st.slider("Average Grade (S1)", 0.0, 20.0, 14.0)
    with col2:
        st.success("**Semester 2 Data**")
        s2_enrolled = st.number_input("Enrolled Units (S2)", value=6)
        s2_approved = st.number_input("Approved Units (S2)", value=6)
        s2_grade = st.slider("Average Grade (S2)", 0.0, 20.0, 14.0)
    
    s1_credited = 0; s1_evals = 6; s1_no_evals = 0; s2_credited = 0; s2_evals = 6; s2_no_evals = 0

with tab4:
    st.subheader("Macro-Economic Impact")
    st.caption("Set the economic conditions during the student's enrollment period:")
    unemp_rate = st.slider("Unemployment rate (%)", 0.0, 20.0, 10.8)
    inflation = st.slider("Inflation rate (%)", 0.0, 5.0, 1.4)
    gdp = st.slider("GDP Growth Rate", -5.0, 5.0, 1.74)

# --- PREDICTION SECTION WITH ANIMATION ---
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("🚀 Analyze Student Profile & Predict", use_container_width=True):
    
    # 1. Visual Progress Bar Animation
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("⚙️ Initializing AI Model...")
    time.sleep(0.5)
    
    progress_bar.progress(30)
    status_text.text("📚 Processing Academic Records...")
    time.sleep(0.5)
    
    progress_bar.progress(60)
    status_text.text("📊 Evaluating Socio-Economic Factors...")
    time.sleep(0.5)
    
    progress_bar.progress(90)
    status_text.text("🧠 Finalizing Prediction...")
    time.sleep(0.5)
    
    progress_bar.progress(100)
    status_text.empty() # Remove the text once done
    
    # 2. Data Preparation
    input_df = pd.DataFrame({
        'Marital status': [marital_status], 'Application mode': [app_mode], 'Application order': [app_order], 'Course': [course],
        'Daytime/evening attendance': [attendance], 'Previous qualification': [prev_qual], 'Previous qualification (grade)': [prev_qual_grade],
        'Nacionality': [nationality], "Mother's qualification": [m_qual], "Father's qualification": [f_qual], "Mother's occupation": [m_occ],
        "Father's occupation": [f_occ], 'Admission grade': [admission_grade], 'Displaced': [displaced], 'Educational special needs': [special_needs],
        'Debtor': [debtor], 'Tuition fees up to date': [tuition_up_to_date], 'Gender': [gender], 'Scholarship holder': [scholarship],
        'Age at enrollment': [age], 'International': [international], 'Curricular units 1st sem (credited)': [s1_credited],
        'Curricular units 1st sem (enrolled)': [s1_enrolled], 'Curricular units 1st sem (evaluations)': [s1_evals],
        'Curricular units 1st sem (approved)': [s1_approved], 'Curricular units 1st sem (grade)': [s1_grade],
        'Curricular units 1st sem (without evaluations)': [s1_no_evals], 'Curricular units 2nd sem (credited)': [s2_credited],
        'Curricular units 2nd sem (enrolled)': [s2_enrolled], 'Curricular units 2nd sem (evaluations)': [s2_evals],
        'Curricular units 2nd sem (approved)': [s2_approved], 'Curricular units 2nd sem (grade)': [s2_grade],
        'Curricular units 2nd sem (without evaluations)': [s2_no_evals], 'Unemployment rate': [unemp_rate], 'Inflation rate': [inflation], 'GDP': [gdp]
    })

    try:
        # Load and Predict
        model = joblib.load("student_model.pkl")
        res = model.predict(input_df)[0]
        
        # 3. Enhanced Output Display
        st.markdown("---")
        st.subheader("🎯 Final AI Report")
        
        if res == 0:
            st.error("## 🚨 Status: CRITICAL RISK (Dropout)")
            st.write("Is student ki profile patterns past dropout students se match karti hain.")
            with st.expander("💡 Actionable Recommendations for Teachers:"):
                st.write("- Student ke saath 1-on-1 counseling session schedule karein.")
                st.write("- Unke low grades ya financial difficulties ko address karein.")
        
        elif res == 1:
            st.warning("## ⚠️ Status: ENROLLED (Struggling)")
            st.write("Student abhi course nahi chhodega, par performance average ya slow ho sakti hai.")
            with st.expander("💡 Actionable Recommendations for Teachers:"):
                st.write("- Student ko extra tutorial classes offer karein.")
                st.write("- Unki academic progress ko regular monitor karein.")
                
        else:
            st.success("## 🎓 Status: SUCCESS (Graduate)")
            st.write("Excellent profile! Ye student bina kisi pareshani ke easily graduate ho jayega.")
            st.balloons()
            with st.expander("💡 Actionable Recommendations for Teachers:"):
                st.write("- Student ko advanced courses ya internships ke liye motivate karein.")
                st.write("- Peer mentoring programs mein inhe leader banayein.")
                
    except FileNotFoundError:
        st.error("❌ 'student_model.pkl' model nahi mila! Kripya apna jupyter model is folder me save karein.")
    except Exception as e:
        st.error(f"⚠️ System Error: {e}")
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_model.pkl")

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# ---------- HEADER ----------
st.markdown("<h2 style='text-align:center;'>❤️ Heart Disease Prediction</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Fill details carefully (hover ⓘ for help)</p>", unsafe_allow_html=True)

st.divider()

# ---------- MAPPINGS ----------
sex_map = {"Male": 1, "Female": 0}

cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "No Symptoms": 3
}

fbs_map = {"No": 0, "Yes": 1}

restecg_map = {
    "Normal": 0,
    "ST-T Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

exang_map = {"No": 0, "Yes": 1}

slope_map = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}

thal_map = {
    "Unknown": 0,
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}

# ---------- BASIC INFO ----------
st.subheader("🧍 Basic Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age", 20, 100, 50,
        help="Age of the patient in years"
    )

with col2:
    sex = sex_map[st.selectbox(
        "Sex",
        list(sex_map.keys()),
        help="Biological sex of the patient"
    )]

# ---------- HEART METRICS ----------
st.subheader("💓 Heart Metrics")
col1, col2 = st.columns(2)

with col1:
    trestbps = st.number_input(
        "Resting BP", 80, 200, 120,
        help="Resting blood pressure (mm Hg). Higher values may indicate hypertension."
    )

    chol = st.number_input(
        "Cholesterol", 100, 600, 200,
        help="Serum cholesterol level (mg/dl). Higher = higher risk."
    )

    thalach = st.number_input(
        "Max Heart Rate", 70, 220, 150,
        help="Maximum heart rate achieved. Lower values may indicate risk."
    )

with col2:
    oldpeak = st.number_input(
        "Oldpeak", 0.0, 6.0, 1.0,
        help="ST depression during exercise. Higher values = more abnormal."
    )

    slope = slope_map[st.selectbox(
        "Slope",
        list(slope_map.keys()),
        help="Slope of ST segment: Downsloping = higher risk"
    )]

    ca = st.selectbox(
        "Major Vessels",
        [0,1,2,3,4],
        help="Number of major vessels. Higher = more blockage risk."
    )

# ---------- MEDICAL CONDITIONS ----------
st.subheader("🩺 Medical Conditions")
col1, col2 = st.columns(2)

with col1:
    cp = cp_map[st.selectbox(
        "Chest Pain Type",
        list(cp_map.keys()),
        help="Type of chest pain. Typical angina is most concerning."
    )]

    exang = exang_map[st.selectbox(
        "Exercise Angina",
        list(exang_map.keys()),
        help="Chest pain during exercise. Yes = higher risk."
    )]

with col2:
    fbs = fbs_map[st.selectbox(
        "High Blood Sugar",
        list(fbs_map.keys()),
        help="Fasting blood sugar >120 mg/dl. Yes indicates diabetes tendency."
    )]

    restecg = restecg_map[st.selectbox(
        "Rest ECG",
        list(restecg_map.keys()),
        help="ECG results. Abnormalities may indicate heart issues."
    )]

    thal = thal_map[st.selectbox(
        "Thalassemia",
        list(thal_map.keys()),
        help="Blood flow condition. Reversible defect = high risk."
    )]

st.divider()

# ---------- PREDICT ----------
if st.button("🔍 Predict Risk", use_container_width=True):

    input_data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal
    ]], columns=[
        "age","sex","cp","trestbps","chol","fbs","restecg",
        "thalach","exang","oldpeak","slope","ca","thal"
    ])

    probs = model.predict_proba(input_data)[0]

    disease_prob = probs[0]

    st.divider()

    if disease_prob > 0.7:
        st.error(f"⚠️ High Risk ({disease_prob*100:.1f}%)")
    elif disease_prob > 0.4:
        st.warning(f"⚠️ Moderate Risk ({disease_prob*100:.1f}%)")
    else:
        st.success(f"✅ Low Risk ({(1-disease_prob)*100:.1f}%)")
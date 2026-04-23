#  Heart Disease Prediction App

A machine learning-powered web application that predicts the likelihood of heart disease based on patient health parameters. Built using Logistic Regression and deployed with Streamlit, this project focuses on both predictive performance and user-friendly interface design.

---

##  Overview

This project uses a classification model trained on structured medical data to estimate the risk of heart disease. The application allows users to input patient details and receive a probability-based risk assessment categorized into Low, Moderate, or High risk.

---

##  Key Features

* Clean and minimal user interface
* Human-readable input fields (no confusing numeric codes)
* Tooltips for each feature to guide users
* Probability-based predictions instead of binary output
* Organized layout for better usability
* Real-time prediction using trained ML model

---

##  Dataset Information

The dataset consists of medical attributes commonly used in heart disease analysis, including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Rest ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak (ST Depression)
* Slope of ST Segment
* Number of Major Vessels
* Thalassemia

The target variable indicates the presence or absence of heart disease.

---

##  Machine Learning Model

* Algorithm: Logistic Regression
* Problem Type: Binary Classification
* Output: Probability of heart disease

Why Logistic Regression?

* More stable and interpretable than complex models
* Provides meaningful probability outputs
* Avoids overfitting on small datasets

---

##  Prediction Logic

The model outputs a probability score which is interpreted as:

* Low Risk → Probability < 0.4
* Moderate Risk → 0.4 to 0.7
* High Risk → > 0.7

This approach provides more nuanced insights compared to simple yes/no predictions.

---

##  User Interface Design

The UI is structured into three logical sections:

*  Basic Information
*  Heart Metrics
*  Medical Conditions

Each input field includes helpful descriptions to ensure accurate data entry and improve prediction reliability.

---

##  Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib

---

##  How to Run Locally

Follow these steps to run the project on your system:

### 1. Clone the Repository
```
git clone https://aydenfromproxima/Heart-Disease-Predictor.git
```
cd Heart-Disease-Predictor

---

### 2. Install Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

---

### 3. Ensure Model File Exists

The trained model file **heart_model.pkl** should be present in the project directory.
If not, run the training script:

python train_model.py

---

### 4. Run the Streamlit App

streamlit run app.py

---

### 5. Open in Browser

After running the command, Streamlit will provide a local URL.
Open it in your browser to access the app.


---


##  Deployment

The application is deployed using Streamlit Cloud and runs entirely in the browser, allowing users to interact with the model in real time.

---

##  Future Improvements

* Add feature importance visualization
* Improve model performance with hyperparameter tuning
* Integrate additional datasets for better generalization
* Add user authentication and history tracking
* Convert into a mobile-friendly interface

---

##  Disclaimer

This application is for educational purposes only and should not be used for medical diagnosis. Always consult a qualified healthcare professional for medical advice.

---

##  Support

If you found this project useful, consider giving it a star and sharing it.

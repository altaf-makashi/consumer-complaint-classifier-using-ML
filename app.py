import streamlit as st
import joblib
import os

# Load the joblib pipeline
@st.cache_resource
def load_model():
    model_path = 'complaint_classifier_pipeline.joblib'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Model file '{model_path}' not found in the repository!")
        return None

pipeline = load_model()

# App UI
st.title("📝 Consumer Complaint Classifier")
st.markdown("Submit a complaint to see which product category it belongs to.")

with st.form("classification_form"):
    complaint = st.text_area("Complaint (Mandatory)*", help="The main body of your complaint.")
    issue = st.text_input("Issue (Optional)")
    sub_issue = st.text_input("Sub-issue (Optional)")
    
    submit = st.form_submit_with_button("Classify Complaint")

if submit:
    if not complaint.strip():
        st.warning("Please provide the mandatory complaint text.")
    elif pipeline:
        # Combine all inputs into one string for the pipeline
        input_data = f"{complaint} {issue} {sub_issue}".strip()
        
        # Prediction
        prediction = pipeline.predict([input_data])[0]
        
        st.success(f"**Predicted Category:** {prediction}")
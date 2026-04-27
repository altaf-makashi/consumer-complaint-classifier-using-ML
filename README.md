# Consumer Complaint Classification System 🚀
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/altaf1021/complaint-classifier)
## 📌 Project Overview
Developed an end-to-end AI system designed to streamline financial grievance handling. This project automatically categorizes ~10,000 unstructured consumer complaints into 16 distinct product sectors (e.g., Mortgages, Credit Reporting, Student Loans) with human-level precision.

By automating the routing of complaints, this solution reduces manual processing time and improves response efficiency for financial institutions.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Machine Learning:** Scikit-learn (`sklearn.pipeline`)
* **Algorithm:** Support Vector Machine (SVM)
* **NLP:** TF-IDF Vectorization (Term Frequency-Inverse Document Frequency)
* **Deployment:** Streamlit & Hugging Face Spaces
* **Data Handling:** Pandas, NumPy

## 💡 Key Technical Features
* **Integrated Scikit-learn Pipeline:** Architected a unified pipeline that encapsulates both the **TF-IDF Vectorizer** and the **SVM Classifier**. This ensures a seamless, reproducible workflow and prevents data leakage during inference.
* **High-Dimensional Feature Engineering:** Transformed raw text into weighted feature matrices, allowing the SVM to find optimal hyperplanes for complex multi-class categorization.
* **Robust Data Preprocessing:** Implemented a data preservation strategy by replacing null values with empty strings rather than trimming rows, maintaining 100% dataset integrity.
* **Performance:** Achieved a peak **classification accuracy of 96.90%**, significantly outperforming baseline models.

## 📁 Project Structure
* **app.py**: The Streamlit web application code for real-time inference.
* **notebooks/**: Contains the full Exploratory Data Analysis (EDA) and model training logic.
* **models/**: Stores the serialized `complaint_classifier_pipeline.joblib` file.
* **requirements.txt**: List of Python dependencies required to run the project.

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer

st.set_page_config(page_title="Ankylosing Spondylitis Detection")

@st.cache_resource
def load_model():
    return joblib.load("hybrid_model.joblib")

@st.cache_resource
def load_feature_names():
    return joblib.load("feature_names.joblib")

model = load_model()
feature_names = load_feature_names()

st.title("Ankylosing Spondylitis Detection (Hybrid RF+MLP Model)")

# FILE UPLOAD
uploaded_file = st.file_uploader("Upload gene expression .xlsx file", type=["xlsx"])

# UTIL: Preprocess and align features
def preprocess_input(df, feature_names):
    # Reindex: add missing columns as NaN, order as in training
    df_reindexed = df.reindex(columns=feature_names)
    n_missing = df_reindexed.isna().all().sum()
    if n_missing > 0:
        st.warning(f"{n_missing} feature columns are missing and will be imputed. "
                   f"If too many are missing, consider checking your file formatting.")
    # Impute missing values in features
    imputer = SimpleImputer(strategy="mean")
    try:
        X_imputed = pd.DataFrame(
            imputer.fit_transform(df_reindexed),
            columns=feature_names,
            index=df.index
        )
    except Exception as e:
        st.error(f"Error during imputation: {e}")
        return None
    return X_imputed

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Preview of uploaded data:", df.head())
        X_input = preprocess_input(df, feature_names)
        if X_input is None:
            st.error("Could not preprocess file. Check for matching columns and file structure.")
        else:
            st.write(f"Number of predictions to make: {X_input.shape[0]}")
            preds = model.predict(X_input)
            # Output per sample (row index as Patient ID, or use another column as needed)
            for idx, label in enumerate(preds):
                patient_id = X_input.index[idx]
                if label == 1:
                    st.error(f"Patient {patient_id} - Ankylosing spondylitis detected")
                else:
                    st.success(f"Patient {patient_id} - Ankylosing spondylitis not detected")
    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a gene expression .xlsx file for prediction.")


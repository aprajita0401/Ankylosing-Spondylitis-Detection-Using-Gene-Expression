import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(page_title="Hybrid Model Predictor", layout="centered")

st.title("Hybrid Model Predictor")

# Adjust this to your model input size
NUM_FEATURES = 4
FEATURE_LABELS = [f"feature_{i+1}" for i in range(NUM_FEATURES)]

MODEL_FILENAME = "hybrid_model.joblib"

@st.cache_resource(show_spinner=False)
def load_model(path=MODEL_FILENAME):
    if not os.path.exists(path):
        st.error(f"Model file not found at {path}. Make sure it's in the repo root.")
        raise FileNotFoundError(path)
    model = joblib.load(path)
    return model

model = None
try:
    model = load_model()
except Exception as e:
    st.stop()

# Build inputs
st.write("Enter feature values (numeric).")
cols = st.columns(NUM_FEATURES)
inputs = []
for i, col in enumerate(cols):
    val = col.number_input(FEATURE_LABELS[i], value=0.0, format="%.6f")
    inputs.append(val)

if st.button("Predict"):
    X = np.array(inputs).reshape(1, -1)
    try:
        pred = model.predict(X)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(X)[0, 1])
        st.success(f"Prediction: {int(pred)}")
        if proba is not None:
            st.info(f"Predicted probability (class 1): {proba:.4f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        raise

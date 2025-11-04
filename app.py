# app.py
import joblib
import numpy as np
import gradio as gr

# Load model (model is in repo root)
model = joblib.load("hybrid_model.joblib")

def predict(features):
    # features will be a list of numbers from the UI
    X = np.array(features).reshape(1, -1)
    pred = model.predict(X)[0]
    proba = None
    if hasattr(model, "predict_proba"):
        proba = float(model.predict_proba(X)[0, 1])
    return {"prediction": int(pred), "probability": proba}

# Build Gradio UI (adapt inputs to your model)
inputs = []
# Example: if model expects 4 numeric features
for i in range(4):
    inputs.append(gr.Number(label=f"feature_{i+1}"))

output = gr.JSON(label="Result")

iface = gr.Interface(fn=predict, inputs=inputs, outputs=output, title="Hybrid Model Predictor")

if __name__ == "__main__":
    iface.launch()

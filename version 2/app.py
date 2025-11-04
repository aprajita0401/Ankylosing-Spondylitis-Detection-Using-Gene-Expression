from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load('./version 2/hybrid_model.joblib') # path to latest model

app = FastAPI()

class Features(BaseModel):
    features: list  # the same length as model's expected input

@app.post("/predict")
def predict(data: Features):
    x = np.array(data.features).reshape(1, -1)
    pred = model.predict(x)[0]
    proba = model.predict_proba(x)[0,1]
    return {"prediction": int(pred), "probability": float(proba)}

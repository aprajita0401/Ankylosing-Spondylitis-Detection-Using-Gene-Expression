# Ankylosing Spondylitis (AS) Detection Using Gene Expression 

## Abstract

This project presents a machine learning-based pipeline for the classification of Ankylosing Spondylitis (AS) patients using gene expression profiles. Two datasets were used: one containing cleaned and normalized gene expression data from AS patients, and the other from healthy controls. Data preparation involved systematic removal of non-informative columns, mean imputation for missing values, consistency and verification of gene identifiers, and feature normalization using z-score scaling. Stratified sampling and SMOTE oversampling were implemented to address class imbalance and ensure robust model training.

Two modeling approaches were developed: Version 1 utilizes a Random Forest classifier with balanced class weights, while Version 2 introduces a hybrid model combining Random Forest with Multi-Layer Perceptron (MLP) through ensemble soft voting. The hybrid model achieved strong performance, with validation and test accuracies of 0.95 and 0.96, respectively, and perfect ROC-AUC scores of 1.0, indicating excellent separability of AS and control samples. The pipeline is production-ready with backend API deployment via FastAPI and seamless integration with web frontends (e.g., Vercel).

This work demonstrates that rigorous data cleaning, normalization, and careful model selection can produce highly accurate gene expression classifiers, facilitating translational research into the diagnosis and molecular understanding of Ankylosing Spondylitis.

---

## File Structure
```
AS_FINAL/
├── dataset/ # Raw and processed gene expression datasets
├── dataset preparation/ # Scripts for cleaning, verification, normalization
│ ├── 1_remove_col.py
│ ├── 2_verification.py
│ ├── 3_missing_values.py
│ ├── 4_verification_missing_data.py
│ ├── 5_cleaned_final.py
│ ├── 6_gene_consistency.py
│ ├── 7_normalised.py
│ └── 8_normalization_verification.py
├── version 1/ # Random Forest model and results
├── version 2/ # Hybrid Random Forest + MLP model
├── app.py # FastAPI backend for predictions
├── requirements.txt # Python dependencies
└── ...
```

---

## Dataset

### Files
- **AS_final_cleaned_normalized.xlsx** – Cleaned and normalized expression data for Ankylosing Spondylitis patients.  
- **normal_final_cleaned_normalized.xlsx** – Cleaned and normalized data for healthy controls.

### Processing Summary
- Removed unwanted annotation columns (only gene expression retained).  
- Verified identical columns, gene IDs, and order between both datasets.  
- Missing values filled using mean imputation per column.  
- Z-score normalization applied (mean ≈ 0, std ≈ 1).  
- Label column (`AS_label`: 1 for AS, 0 for normal) added during model training.  

---

## Data Preparation Workflow
Scripts in `/dataset preparation/` execute the full data pipeline:

1. **1_remove_col.py** – Drops unnecessary annotation columns.  
2. **2_verification.py** – Ensures column alignment between datasets.  
3. **3_missing_values.py** – Fills missing values using mean imputation.  
4. **4_verification_missing_data.py** – Confirms no missing values remain.  
5. **5_cleaned_final.py** – Outputs cleaned datasets ready for modeling.  
6. **6_gene_consistency.py** – Checks probe/gene ID consistency.  
7. **7_normalised.py** – Applies z-score normalization.  
8. **8_normalization_verification.py** – Validates normalization metrics.

---

## Models

### Version 1: Random Forest
- Trained with stratified 70/15/15 split (train/validation/test).  
- Uses all numeric gene expression features.  
- `class_weight='balanced'` to mitigate class imbalance.  
- Evaluation metrics: Precision, Recall, F1-score, ROC-AUC, Feature Importance.

### Version 2: Hybrid Random Forest + Multi-Layer Perceptron
- Ensemble model combining Random Forest and MLP using **soft voting**.  
- Same preprocessing pipeline as Version 1, plus SMOTE balancing.  
- Trained and validated on stratified data splits.  
- Latest and best-performing model, served via FastAPI backend.

---

## Results (Version 2 Hybrid Model)

| Metric | Normal | AS | Accuracy | ROC-AUC |
|---------|--------|----|-----------|---------|
| **Precision (Validation)** | 0.92 | 1.00 | 0.95 | 1.00 |
| **Recall (Validation)** | 1.00 | 0.91 |  |  |
| **F1-Score (Validation)** | 0.96 | 0.95 |  |  |
| **Precision (Test)** | 0.92 | 1.00 | 0.96 | 1.00 |
| **Recall (Test)** | 1.00 | 0.91 |  |  |
| **F1-Score (Test)** | 0.96 | 0.95 |  |  |

**Interpretation:**  
The hybrid model demonstrates near-perfect separation between AS and control classes, with excellent precision, recall, and ROC-AUC scores.

---

## Deployment

### Backend

- FastAPI service (`app.py`) loads `version 2/hybrid_model.joblib`.  
- Endpoint: `/predict` (POST) for classification requests.

**Example Request:**
```json
{
  "features": [1.1, 2.2, 3.3]
}
```
**Example Response:**
```json
{
  "prediction": "AS",
  "probability": 0.95
}
```
### Frontend

- Deployed via Vercel (Next.js / React).
- Sends POST requests to the backend for live predictions.

**Example (JavaScript):**
```javascript
const response = await fetch("https://your-backend-domain/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ features: [/* feature values */] })
});
const result = await response.json();
console.log(result.prediction, result.probability);
```

---

## Requirements

**Listed in requirements.txt:**

- fastapi
- uvicorn
- scikit-learn
- joblib
- numpy

---

## Quick Start

- Run preprocessing scripts from /dataset preparation/ in sequence.
- Train models using scripts in /version 1/ or /version 2/.
- Save final model as hybrid_model.joblib in /version 2/.
- Deploy FastAPI backend with app.py.
- Connect frontend to /predict endpoint for real-time inference.

---

## License

- This project is for research and academic use only.
- For clinical or production applications, independent validation is required.








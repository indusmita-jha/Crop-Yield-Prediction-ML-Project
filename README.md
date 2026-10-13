# 🌾 Crop Yield Predictor with Smart Recommendations

A machine learning-powered web application that predicts crop yield based on agricultural inputs and provides actionable farming recommendations.

---

## 👩‍💻 Authors

| Name | Roll Number |
|------|-------------|
| **Raveena** | 2427030606 |
| **Indusmita Jha** | 2427030436 |

---

## 📌 Project Overview

This project uses an **XGBoost regression model** trained on Indian agricultural data to predict crop yield (in tonnes per hectare). The model takes into account crop type, growing season, state, area, rainfall, fertilizer usage, and pesticide usage to generate predictions and personalized farming advice.

The interactive UI is built using **Gradio**, making it easy to use without any coding knowledge.

---

## 🚀 Features

- 🌱 Predict crop yield (t/ha) for **50+ Indian crops**
- 🗺️ Supports **30 Indian states**
- 🌤️ Handles **6 growing seasons** (Kharif, Rabi, Whole Year, Autumn, Summer, Winter)
- 💡 Smart recommendations based on:
  - Rainfall levels
  - Fertilizer per hectare ratio
  - Pesticide per hectare ratio
- 🖥️ Clean and interactive Gradio web interface

---

## 🗂️ Project Structure

```
PA Project/
│
├── app.py                   # Gradio web app — main entry point
├── brain.py                 # Prediction logic & recommendation engine
├── prediction_training.py   # Model training script (XGBoost + GridSearchCV)
├── cleaning.ipynb           # Data cleaning & preprocessing notebook
├── pred_model.pkl           # Pre-trained XGBoost model (serialized)
└── README.md                # Project documentation
```

---

## 🧠 Model Details

| Property | Value |
|----------|-------|
| Algorithm | XGBoost Regressor |
| Hyperparameter Tuning | GridSearchCV with 5-Fold Cross-Validation |
| Target Variable | `Yield` (tonnes per hectare) |
| Encoding | One-Hot Encoding for categorical features |
| Serialization | `joblib` (`.pkl`) |

**Tuned Hyperparameters searched:**
- `max_depth`: [3, 4, 5]
- `learning_rate`: [0.05, 0.1]
- `n_estimators`: [100, 200]
- `subsample`, `colsample_bytree`, `gamma`, `min_child_weight`

---

## 📥 Input Features

| Feature | Type | Description |
|---------|------|-------------|
| Crop | Dropdown | Type of crop (e.g., Rice, Wheat, Maize) |
| Season | Dropdown | Growing season (e.g., Kharif, Rabi) |
| State | Dropdown | Indian state |
| Area | Number | Area under cultivation (hectares) |
| Annual Rainfall | Number | Total annual rainfall (mm) |
| Fertilizer Usage | Number | Total fertilizer used (kg) |
| Pesticide Usage | Number | Total pesticide used (kg) |

---

## 📤 Outputs

| Output | Description |
|--------|-------------|
| Predicted Yield | Estimated yield in tonnes per hectare (t/ha) |
| Recommendations | Actionable farming advice based on input ratios |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies

```bash
pip install gradio xgboost scikit-learn pandas joblib numpy
```

### Run the App

```bash
python app.py
```

Then open your browser and go to: `http://localhost:8888`

---

## 📊 Recommendation Logic

| Condition | Advice |
|-----------|--------|
| Rainfall < 500 mm | ⚠️ Consider increasing irrigation |
| Rainfall > 3000 mm | 💧 Ensure proper drainage |
| Fertilizer/ha < 100 kg | 🌱 Consider soil enrichment |
| Fertilizer/ha > 1000 kg | 🧪 Check for nutrient overload |
| Pesticide/ha > 50 kg | 🐞 Monitor for resistance or overuse |
| All inputs balanced | ✅ Maintain current practices |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| XGBoost | ML model |
| scikit-learn | Model training, evaluation, cross-validation |
| Gradio | Web UI |
| pandas | Data manipulation |
| joblib | Model serialization |
| Jupyter Notebook | Data cleaning & EDA |

---

## 📄 License

This project was developed as part of an academic assignment. All rights reserved by the authors.

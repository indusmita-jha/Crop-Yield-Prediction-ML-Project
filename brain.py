import joblib
import pandas as pd

# Load model once globally
model = joblib.load("pred_model.pkl")
expected_features = model.get_booster().feature_names

def predict_crop_yield_with_advice(crop, season, state, area, rainfall, fertilizer, pesticide):
    """
    Predict crop yield and provide recommendations based on input ratios.
    """

    # Build input dictionary
    input_data = {
        'Crop': crop,
        'Season': season,
        'State': state,
        'Area': area,
        'Annual_Rainfall': rainfall,
        'Fertilizer': fertilizer,
        'Pesticide': pesticide
    }

    # Convert to DataFrame
    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)

    # Add missing columns
    for col in expected_features:
        if col not in df_encoded:
            df_encoded[col] = 0

    # Reorder columns
    df_encoded = df_encoded[expected_features]

    # Predict yield
    prediction = model.predict(df_encoded)[0]

    # Calculate per unit area metrics
    fert_per_hectare = fertilizer / area if area else 0
    pest_per_hectare = pesticide / area if area else 0

    # Generate recommendations
    recommendations = []

    if rainfall < 500:
        recommendations.append("⚠️ Rainfall is low — consider increasing irrigation.")
    elif rainfall > 3000:
        recommendations.append("💧 Excess rainfall — ensure proper drainage.")

    if fert_per_hectare < 100:
        recommendations.append("🌱 Fertilizer per hectare is low — consider soil enrichment.")
    elif fert_per_hectare > 1000:
        recommendations.append("🧪 Fertilizer per hectare is very high — check for nutrient overload.")

    if pest_per_hectare > 50:
        recommendations.append("🐞 High pesticide per hectare — monitor for resistance or overuse.")

    if not recommendations:
        recommendations.append("✅ Inputs look balanced — maintain current practices.")

    return round(prediction, 4), "\n".join(recommendations)
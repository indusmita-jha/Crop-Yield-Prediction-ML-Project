import gradio as gr
from brain import predict_crop_yield_with_advice


# crop_options = ['paarth', 'virat']

# season_options = ['ritvik']

# state_options = ['gargi']

# Crop list
crops = [
    "Arecanut",
    "Arhar/Tur",
    "Castor seed",
    "Cotton(lint)",
    "Dry chillies",
    "Gram",
    "Jute",
    "Linseed",
    "Maize",
    "Mesta",
    "Niger seed",
    "Onion",
    "Other Rabi pulses",
    "Potato",
    "Rapeseed &Mustard",
    "Rice",
    "Sesamum",
    "Small millets",
    "Sugarcane",
    "Sweet potato",
    "Tapioca",
    "Tobacco",
    "Turmeric",
    "Wheat",
    "Bajra",
    "Black pepper",
    "Coriander",
    "Garlic",
    "Ginger",
    "Groundnut",
    "Horse-gram",
    "Jowar",
    "Ragi",
    "Cashewnut",
    "Banana",
    "Soyabean",
    "Barley",
    "Khesari",
    "Masoor",
    "Moong(Green Gram)",
    "Other Kharif pulses",
    "Safflower",
    "Sannhamp",
    "Urad",
    "Peas & beans (Pulses)",
    "Sunflower",
    "Cardamom",
    "other oilseeds",
    "Other Cereals",
    "Cowpea(Lobia)",
    "Oilseeds total",
    "Guar seed",
    "Other Summer Pulses",
    "Moth",
    "Coconut"
]

# State list
states = [
    "Assam",
    "Karnataka",
    "Kerala",
    "Meghalaya",
    "West Bengal",
    "Puducherry",
    "Goa",
    "Andhra Pradesh",
    "Tamil Nadu",
    "Odisha",
    "Bihar",
    "Gujarat",
    "Madhya Pradesh",
    "Maharashtra",
    "Mizoram",
    "Punjab",
    "Uttar Pradesh",
    "Haryana",
    "Himachal Pradesh",
    "Tripura",
    "Nagaland",
    "Chhattisgarh",
    "Uttarakhand",
    "Jharkhand",
    "Delhi",
    "Manipur",
    "Jammu and Kashmir",
    "Telangana",
    "Arunachal Pradesh",
    "Sikkim"
]

# Season list
seasons = [
    "Whole Year",
    "Kharif",
    "Rabi",
    "Autumn",
    "Summer",
    "Winter"
]

demo = gr.Interface(
    fn=predict_crop_yield_with_advice,
    inputs=[
        gr.Dropdown(choices=crops, label="Crop"),
        gr.Dropdown(choices=seasons, label="Season"),
        gr.Dropdown(choices=states, label="State"),
        gr.Number(label="Area (in hectares)"),
        gr.Number(label="Annual Rainfall (mm)"),
        gr.Number(label="Fertilizer Usage (kg)"),
        gr.Number(label="Pesticide Usage (kg)")
    ],
    outputs=[
        gr.Number(label="Predicted Yield (t/ha)"),
        gr.Textbox(label="Recommendations", lines=6)
    ],
    title="🌾 Crop Yield Predictor + Smart Recommendations",
    description="Enter your crop details to get an estimated yield and actionable farming advice."
)

demo.launch(debug='True', server_port=8888)
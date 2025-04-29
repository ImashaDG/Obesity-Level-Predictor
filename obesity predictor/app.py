import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load trained model and scaler
model = joblib.load("obesity_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title and Instructions
st.title("Obesity Level Predictor 🍔🧠")
st.write("Fill out the details below to get your BMI, obesity level, meal suggestions, and exercise plan.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 100)
height = st.number_input("Height (in meters)", min_value=1.0, step=0.01)
weight = st.number_input("Weight (in kg)", min_value=10.0, step=0.1)
family_history = st.selectbox("Family History of Overweight?", ["yes", "no"])
favc = st.selectbox("Do you frequently consume high-calorie food? (FAVC)", ["yes", "no"])
fcvc = st.slider("Frequency of Vegetable Consumption (1-3)", 1, 3)
ncp = st.slider("Number of Main Meals per Day", 1, 4)
caec = st.selectbox("Food Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you smoke?", ["yes", "no"])
ch2o = st.slider("Daily Water Intake (CH2O) (1-3)", 1, 3)
scc = st.selectbox("Do you monitor your calorie intake? (SCC)", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (FAF) (0-3)", 0, 3)
tue = st.slider("Time Using Technology Devices (TUE) (0-3)", 0, 3)
calc = st.selectbox("Alcohol Consumption (CALC)", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Main Mode of Transport (MTRANS)", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])

# Helper functions
def encode_input():
    """Encodes input data into model-compatible format."""
    return [
        1 if gender == "Male" else 0,
        age,
        height,
        weight,
        1 if family_history == "yes" else 0,
        1 if favc == "yes" else 0,
        fcvc,
        ncp,
        0 if caec == "no" else 1 if caec == "Sometimes" else 2 if caec == "Frequently" else 3,
        1 if smoke == "yes" else 0,
        ch2o,
        1 if scc == "yes" else 0,
        faf,
        tue,
        0 if calc == "no" else 1 if calc == "Sometimes" else 2 if calc == "Frequently" else 3,
        0 if mtrans == "Automobile" else 1 if mtrans == "Bike" else 2 if mtrans == "Motorbike" else 3 if mtrans == "Public_Transportation" else 4
    ]

def calculate_bmi(weight, height):
    """Calculates BMI."""
    return round(weight / (height ** 2), 2)

def get_meal_ideas(bmi):
    """Suggests meal plans based on BMI."""
    if bmi < 18.5:
        return "High-calorie meals: Avocado toast, peanut butter smoothies, nuts, and dairy-rich dishes."
    elif 18.5 <= bmi < 24.9:
        return "Balanced meals: Grilled chicken, quinoa, mixed greens, and fruit salads."
    elif 25 <= bmi < 29.9:
        return "Low-calorie meals: Stir-fried vegetables, baked fish, and salads with vinaigrette."
    else:
        return "Very low-calorie meals: Steamed vegetables, soups, and lean proteins like tofu or chicken breast."

def get_exercise_plan(bmi):
    """Suggests exercise plans based on BMI."""
    if bmi < 18.5:
        return "Light exercises: Yoga, stretching, and light weightlifting."
    elif 18.5 <= bmi < 24.9:
        return "Moderate exercises: Jogging, cycling, and swimming."
    elif 25 <= bmi < 29.9:
        return "High-intensity exercises: Cardio, HIIT, and strength training."
    else:
        return "Low-impact exercises: Walking, water aerobics, and resistance training."

# Predict and display results
if st.button("Predict"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        input_data = np.array([encode_input()])
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)

        # Display BMI
        st.subheader("Your BMI")
        st.write(f"Your BMI is **{bmi}**")

        # Practical BMI Visualization
        st.subheader("BMI Visualization")
        fig, ax = plt.subplots(figsize=(8, 3))
        categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
        ranges = [18.5, 24.9, 29.9, 40]
        colors = ["blue", "green", "orange", "red"]

        start = 0
        for i, range_value in enumerate(ranges):
            # Draw the BMI range bar
            ax.barh(0, range_value - start, left=start, color=colors[i], edgecolor="black", height=0.5)
            start = range_value

        ax.axvline(x=bmi, color="black", linestyle="--", label=f"Your BMI: {bmi}")
        ax.set_yticks([])
        ax.set_xlim(0, 40)
        ax.set_xticks([0, 18.5, 24.9, 29.9, 40])
        ax.set_xticklabels(["0", "18.5", "24.9", "29.9", "40"])
        ax.legend(loc="upper left")
        ax.set_xlabel("BMI Range")
        st.pyplot(fig)

        # Recommendations
        st.subheader("Recommended Meal Plan")
        st.write(get_meal_ideas(bmi))

        st.subheader("Recommended Exercise Plan")
        st.write(get_exercise_plan(bmi))

        # Prediction Result
        st.success(f"Predicted Obesity Category: **{prediction[0]}**")
    else:
        st.error("Please enter valid height and weight.")
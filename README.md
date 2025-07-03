# Obesity-Level-Predictor
The project aimed to predict obesity levels (e.g., normal weight, overweight, obese) based on individual health and lifestyle data such as age, weight, physical activity, calorie intake, and eating habits. This can assist healthcare professionals or individuals in taking early preventive action or adjusting lifestyle behaviors.

Techniques Used:
This was a supervised learning task where I compared multiple classification algorithms:

Logistic Regression – as a baseline linear classifier

K-Nearest Neighbors (KNN) – to find similar health profiles

Decision Tree – for interpretability

Random Forest – for better accuracy through ensemble learning

The dataset was preprocessed using Label Encoding, StandardScaler, and train-test split. I used accuracy, precision, recall, F1-score, and confusion matrices for evaluation. The best-performing model was deployed in a Streamlit web app that takes user inputs and returns predicted obesity levels with practical health suggestions.

Challenges Faced:

Handling imbalanced class distribution in the target variable.

Ensuring consistent encoding and scaling between training and Streamlit inputs.

Managing version conflicts while loading .pkl models due to scikit-learn updates.

Making the UI user-friendly while preserving model accuracy and robustness.

References:
Link to the Data set-https://www.kaggle.com/datasets/adeniranstephen/obesity-prediction-dataset

Link to the Notebook- https://colab.research.google.com/drive/1N-WrYcj2Nr7hy2bouv2kgYxT8wCosyX4?usp=sharing

Link to the Youtube Video - https://youtu.be/ZUaM-3eQ-24

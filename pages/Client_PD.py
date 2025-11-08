import numpy as np
import pandas as pd
import streamlit as st
from joblib import load



# Charger le modèle

path_model = "C:/Users/ramas/OneDrive/Desktop/BankAttritionFlow/models/best_lr_model.pkl"

with open(path_model, "rb") as f:
    model = load(f)



st.title("💳 Prédiction de churn bancaire")

# Entrées utilisateur
credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")
salary = st.number_input("Estimated Salary")
tenure = st.number_input("Tenure")
num_products = st.number_input("Num of Products")
has_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
gender = st.selectbox("Gender", ["Male", "Female"])
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])

# Encodage manuel
gender_map = {'Male': 0, 'Female': 1}
geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}

data = pd.DataFrame([{
    'CreditScore': credit_score,
    'Age': age,
    'Balance': balance,
    'EstimatedSalary': salary,
    'Tenure': tenure,
    'NumOfProducts': num_products,
    'HasCrCard': has_card,
    'IsActiveMember': is_active,
    'Gender_Index': gender_map[gender],
    'Geography_Index': geography_map[geography]
}])

# Réordonner les colonnes si nécessaire
feature_cols = [
    'CreditScore', 'Age', 'Balance', 'EstimatedSalary',
    'Tenure', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'Geography_Index', 'Gender_Index'
]
data = data[feature_cols]


# Prédiction
if st.button("Prédire"):
    pred_class = model.predict(data)[0]
    # pred_prob = model.predict_proba(data)[0][1]
    
    if pred_class == 1:
        res = "Oui"
    else:
        res = "Non"

    st.subheader("Résultat :")
    st.write(f"✅ Prédit l'attrition des client : {res}")
    # st.write(f"📊 Probabilité de churn : {pred_prob:.2f}")

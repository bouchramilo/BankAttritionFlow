import streamlit as st
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from pyspark.sql.functions import lit
import os
import sys

st.set_page_config(
    page_title="Prédiction",
    page_icon="💳",
    layout='wide'
)

st.title("💳 Prédiction de l'Attrition Client Bancaire")


# Configuration des variables d'environnement Python
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# --------------------------
spark = SparkSession.builder \
    .appName("MongoDB-PySpark-PyMongo") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.python.worker.timeout", "600") \
    .master("local[*]") \
    .getOrCreate()
    # .config("spark.hadoop.io.nativeio.NativeIO$Windows.enabled", "false") \
    



# --------------------------


st.write("Entrez les informations du client :")

credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
balance = st.number_input("Balance", min_value=0.0, value=5000.0)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=3)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=10, value=2)
has_cr_card = st.selectbox("Has Credit Card ?", [0, 1])
is_active_member = st.selectbox("Is Active Member ?", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)


# --------------------------
# Préparer le DataFrame Spark

data_dict = [{
    "CreditScore": credit_score,
    "Age": age,
    "Balance": balance,
    "Tenure": tenure,
    "NumOfProducts": num_of_products,
    "HasCrCard": has_cr_card,
    "IsActiveMember": is_active_member,
    "EstimatedSalary": estimated_salary
}]

df_new = spark.createDataFrame(data_dict)


# --------------------------
# Charger le modèle
model_path = "C:/tmp/best_lr_model"
loaded_model = PipelineModel.load(model_path)


# --------------------------
# Prédiction

if st.button("Prédire"):
    preds = loaded_model.transform(df_new)
    result = preds.select("prediction", "probability").collect()[0]
    pred_class = int(result["prediction"])
    pred_prob = float(result["probability"][1])

    st.subheader("Résultat :")
    st.write(f"✅ Prédit churn : {pred_class} (1 = churn, 0 = pas de churn)")
    st.write(f"📊 Probabilité de churn : {pred_prob:.2f}")

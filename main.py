import streamlit as st

st.set_page_config(
    page_title="title page",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Prédiction de l'Attrition Client Bancaire")

st.markdown("""
### Contexte du projet
Dans le secteur bancaire, il est important d'anticiper la perte de clients pour réduire le taux d'attrition et améliorer la fidélisation.  
Ce projet utilise **PySpark** pour traiter de grandes quantités de données, **MLlib** pour entraîner un modèle prédictif, **MongoDB** pour stocker les données préparées, et **Streamlit** pour visualiser les résultats et faciliter la prise de décision.

### Étapes principales du projet
1. **Configuration de Spark** : Initialisation de Spark pour le traitement des données.  
2. **Chargement des données** : Import des données brutes dans un DataFrame Spark.  
3. **Analyse exploratoire (EDA)** : Étude des données, statistiques descriptives et détection des valeurs manquantes ou anomalies.  
4. **Prétraitement des données** : Nettoyage, encodage des variables catégorielles et transformation des features.  
5. **Stockage intermédiaire** : Sauvegarde des données préparées dans MongoDB pour un usage futur.  
6. **Construction du pipeline ML** : Assemblage des features, gestion du déséquilibre des classes, normalisation et préparation du modèle.  
7. **Entraînement et validation** : Optimisation des hyperparamètres via CrossValidator et évaluation avec BinaryClassificationEvaluator.  
8. **Évaluation du modèle** : Calcul des métriques (AUC-ROC, Accuracy, Precision, Recall, F1-score) et analyse de la matrice de confusion.  
9. **Déploiement** : Sauvegarde du modèle et création d'une interface de prédiction en temps réel avec Streamlit.
""")

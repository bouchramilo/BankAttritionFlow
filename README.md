# 💳 Prédiction de l'Attrition Client Bancaire

## Contexte du projet
Dans le secteur bancaire, anticiper la perte de clients est essentiel pour réduire le taux d’attrition et améliorer la fidélisation.  
Ce projet utilise des données clients pour entraîner un modèle prédictif capable de détecter les clients susceptibles de quitter la banque.  
L’interface Streamlit permet de faire des prédictions en temps réel pour de nouveaux clients.

---

## ⚡ Étapes principales du projet
1. **Initialisation de Spark** : configuration de la session Spark pour le traitement distribué.  
2. **Chargement des données** : import des données brutes au format CSV.  
3. **Analyse exploratoire (EDA)** : statistiques descriptives, valeurs manquantes et outliers.  
4. **Prétraitement** : nettoyage, encodage des variables catégorielles, transformations (ex: log1p sur l’âge).  
5. **Stockage intermédiaire** : sauvegarde des données prétraitées dans MongoDB.  
6. **Pipeline ML** : assemblage des features, gestion du déséquilibre, normalisation et préparation du modèle.  
7. **Entraînement et validation** : optimisation des hyperparamètres et évaluation des performances.  
8. **Évaluation finale** : calcul des métriques (AUC-ROC, Accuracy, Precision, Recall, F1-score) et matrice de confusion.  
9. **Déploiement** : sauvegarde du modèle et interface de prédiction en temps réel avec Streamlit.


---

## 🛠 Outils et technologies
- **Python**  
- **PySpark** : traitement de grands volumes de données  
- **MLlib** : création et entraînement du modèle de machine learning  
- **MongoDB** : stockage des données préparées  
- **Streamlit** : interface web pour visualiser et prédire  
- **Pandas & NumPy** : manipulation des données pour l’interface  

---

## 📥 Cloner le projet
```bash
git clone https://github.com/bouchramilo/BankAttritionFlow.git
cd BankAttritionFlow
```

---

## 🚀 Lancer l’interface Streamlit

```bash
streamlit run main.py
```

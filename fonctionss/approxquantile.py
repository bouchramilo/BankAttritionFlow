import pandas as pd
import numpy as np
from pyspark.sql import functions as F
from fonctionss.viz import viz, viz_all, visualization


def outliers_detections_cols(df, cols, prob_lower=0.25, prob_upper=0.75, low_bnd=1.5, upp_bnd=1.5):
    """
    Calcule les bornes IQR et le nombre d'outliers pour chaque colonne.
    Retourne une liste de tuples : (col, q1, q3, iqr, lower, upper, total)
    """
    reports = []

    for c in cols:
        q1, q3 = df.approxQuantile(c, [prob_lower, prob_upper], 0.01)
        iqr = q3 - q1
        lower_bound = q1 - low_bnd * iqr
        upper_bound = q3 + upp_bnd * iqr

        count_lower = df.filter(F.col(c) < lower_bound).count()
        count_upper = df.filter(F.col(c) > upper_bound).count()
        total = count_lower + count_upper
        
        print("=*="*50)
        print(f"{c}")
        print("=*="*50)
        print("Q1 (25%) : ", q1)
        print("Q3 (75%) : ", q3)
        print("IQR : ", iqr)
        print(f"Total outlier : ", total)
        
        pdf = df.toPandas()
        
        visualization(pdf, c, lower_bound, upper_bound)
    

        reports.append((c, q1, q3, iqr, lower_bound, upper_bound, total))

    return pd.DataFrame(reports, columns=["col", "Q1", "Q3", "IQR", "lower", "upper", "outliers_total"])




def outliers_detection_col(df, colo, prob_lower=0.25, prob_upper=0.75, low_bnd=1.5, upp_bnd=1.5):
    """
    Calcule les bornes IQR et le nombre d'outliers pour une seule colonne.
    """
    q1, q3 = df.approxQuantile(colo, [prob_lower, prob_upper], 0.01)
    iqr = q3 - q1

    lower_bound = q1 - low_bnd * iqr
    upper_bound = q3 + upp_bnd * iqr

    count_lower = df.filter(F.col(colo) < lower_bound).count()
    count_upper = df.filter(F.col(colo) > upper_bound).count()
    total = count_lower + count_upper
    
    print("=*="*50)
    print(f"{colo}")
    print("=*="*50)
    print("Q1 (25%) : ", q1)
    print("Q3 (75%) : ", q3)
    print("IQR : ", iqr)
    print(f"Total outlier : ", total)
    
    pdf = df.toPandas()
    
    visualization(pdf, colo, lower_bound, upper_bound)
    
    reports = [(colo, q1, q3, iqr, lower_bound, upper_bound, total)]

    return pd.DataFrame(reports, columns=["col", "Q1", "Q3", "IQR", "lower", "upper", "outliers_total"])



def visualize_outliers(df_spark, cols, prob_lower=0.25, prob_upper=0.75):
    """
    Combine les calculs Spark et la visualisation matplotlib.
    """

    reports = outliers_detections_cols(df_spark, cols, prob_lower, prob_upper)

    pdf = df_spark.toPandas()

    bounds = {r[0]: (r[4], r[5]) for r in reports}

    viz_all(pdf, cols, show_iqr=True, bounds_dict=bounds)

    return pd.DataFrame(reports, columns=["col", "Q1", "Q3", "IQR", "lower", "upper", "outliers_total"])

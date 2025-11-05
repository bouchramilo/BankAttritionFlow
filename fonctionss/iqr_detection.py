import pandas as pd
import numpy as np
from pyspark.sql import functions as F
from fonctionss.viz import viz, viz_all


def outliers_detections_cols(df, cols, prob_lower=0.25, prob_upper=0.75):
    """
    Calcule les bornes IQR et le nombre d'outliers pour chaque colonne.
    Retourne une liste de tuples : (col, q1, q3, iqr, lower, upper, total)
    """
    reports = []

    for c in cols:
        q1, q3 = df.approxQuantile(c, [prob_lower, prob_upper], 0.01)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        count_lower = df.filter(F.col(c) < lower_bound).count()
        count_upper = df.filter(F.col(c) > upper_bound).count()
        total = count_lower + count_upper

        reports.append((c, q1, q3, iqr, lower_bound, upper_bound, total))

    return reports




def outliers_detection_col(df, c, prob_lower=0.25, prob_upper=0.75):
    """
    Calcule les bornes IQR et le nombre d'outliers pour une seule colonne.
    """
    q1, q3 = df.approxQuantile(c, [prob_lower, prob_upper], 0.01)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    count_lower = df.filter(F.col(c) < lower_bound).count()
    count_upper = df.filter(F.col(c) > upper_bound).count()
    total = count_lower + count_upper

    return [(c, q1, q3, iqr, lower_bound, upper_bound, total)]




def visualize_outliers(df_spark, cols, prob_lower=0.25, prob_upper=0.75):
    """
    Combine les calculs Spark et la visualisation matplotlib.
    """

    reports = outliers_detections_cols(df_spark, cols, prob_lower, prob_upper)

    pdf = df_spark.toPandas()

    bounds = {r[0]: (r[4], r[5]) for r in reports}

    viz_all(pdf, cols, show_iqr=True, bounds_dict=bounds)

    return pd.DataFrame(reports, columns=["col", "Q1", "Q3", "IQR", "lower", "upper", "outliers_total"])

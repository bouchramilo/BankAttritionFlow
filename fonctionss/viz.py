import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ! *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def viz(data, col, show_iqr=False, lower_bound=None, upper_bound=None):
    
    plt.figure(figsize=(8, 5))
    plt.hist(data[col], bins=20, color='#69b3a2', edgecolor='black', alpha=0.7)

    if show_iqr:
        if lower_bound is not None or upper_bound is not None:
            plt.axvline(lower_bound, color='red', linestyle='--', linewidth=2, label='Limite inférieure (IQR)')
            plt.axvline(upper_bound, color='red', linestyle='--', linewidth=2, label='Limite supérieure (IQR)')
            plt.legend()
            


    plt.title(f"Distribution de {col}", fontsize=14, fontweight='bold')
    plt.xlabel(col, fontsize=12)
    plt.ylabel("Fréquence", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


# ! *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def viz_all(data, cols, show_iqr=False, bounds_dict=None):
    
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 14))
    axes = axes.flatten()

    for i, col in enumerate(cols[:6]):
        axes[i].hist(data[col], bins=20, color='#69b3a2', edgecolor='black', alpha=0.7)

        if show_iqr:
            if bounds_dict and col in bounds_dict:
                lower_bound, upper_bound = bounds_dict[col]

                axes[i].axvline(lower_bound, color='red', linestyle='--', linewidth=2)
                axes[i].axvline(upper_bound, color='red', linestyle='--', linewidth=2)

        axes[i].set_title(col)
        axes[i].grid(axis='y', linestyle='--', alpha=0.6)

    plt.suptitle("Histogrammes des variables numériques", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()



# ! *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def visualization(data, column, lower_limit=None, upper_limit=None):
    """Affiche un boxplot et un histogramme KDE pour la colonne donnée.

    Args:
        data (pd.DataFrame): le DataFrame contenant la colonne.
        column (str): nom de la colonne à tracer.
        lower_limit (float|None): ligne horizontale inférieure (optionnelle).
        upper_limit (float|None): ligne horizontale supérieure (optionnelle).
    """
    fig, axes = plt.subplots(1, 2, figsize=(18, 5))

    # BoxPlot (avec des limites si définies)
    sns.boxplot(data=data, y=column, ax=axes[0], color="skyblue")

    if upper_limit is not None:
        axes[0].axhline(y=upper_limit, color="red", linestyle="--", linewidth=1, label=f"Limit sup:{upper_limit:.2f}")
    if lower_limit is not None:
        axes[0].axhline(y=lower_limit, color="red", linestyle="--", linewidth=1, label=f"Limit inf:{lower_limit:.2f}")
        
    max_v = data[column].max()
    min_v = data[column].min()
    if max_v is not None:
        axes[0].axhline(y=max_v, color="green", linestyle="--", linewidth=1, label=f"Limit max_v:{max_v:.2f}")
    if min_v is not None:
        axes[0].axhline(y=min_v, color="green", linestyle="--", linewidth=1, label=f"Limit min_v:{min_v:.2f}")

    axes[0].set_title(f"Boxplot de {column}")
    try:
        axes[0].legend()
    except Exception:
        pass

    # Histogramme avec KDE (et Limites si définies)
    sns.histplot(data[column], kde=True, ax=axes[1], color="orange")

    if upper_limit is not None:
        axes[1].axvline(x=upper_limit, color="red", linestyle="--", linewidth=1, label=f"Limit sup:{upper_limit:.2f}")
    if lower_limit is not None:
        axes[1].axvline(x=lower_limit, color="red", linestyle="--", linewidth=1, label=f"Limit inf:{lower_limit:.2f}")
    
    
    max_v = data[column].max()
    min_v = data[column].min()
    if max_v is not None:
        axes[1].axvline(x=max_v, color="green", linestyle="--", linewidth=1, label=f"Limit max_v:{max_v:.2f}")
    if min_v is not None:
        axes[1].axvline(x=min_v, color="green", linestyle="--", linewidth=1, label=f"Limit min_v:{min_v:.2f}")
    
    axes[1].set_title(f"Distribution de {column}")
    try:
        axes[1].legend()
    except Exception:
        pass

    plt.title(f"{column}")
    plt.tight_layout()
    plt.show()
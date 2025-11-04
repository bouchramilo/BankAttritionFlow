import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

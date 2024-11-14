import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

plt.switch_backend('Agg')

def heatmap_matrix(df, matrix, filename="backend/public/images/heatmap.png"):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
    plt.title(f'Heatmap')
    plt.savefig(filename)
    plt.close()

def main(file_path):
    # Read the CSV file for the selected river
    df = pd.read_csv(file_path)

    # Replace 'BDL' with NaN
    df.replace('BDL', np.nan, inplace=True)

    # Convert all columns to numeric, forcing non-numeric values to NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Compute the Pearson correlation matrix
    pearson_corr = df.corr(method='pearson').round(2)

    # Generate and save the heatmap
    heatmap_matrix(df, pearson_corr, "backend/public/images/heatmap.png")

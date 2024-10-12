import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set Matplotlib to use the 'Agg' backend for non-GUI rendering
plt.switch_backend('Agg')

# Function to generate and save heatmap
def heatmap_matrix(df, matrix, filename="backend/public/images/heatmap.png"):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.figure(figsize=(10, 8))  # Set the figure size
    sns.heatmap(matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
    plt.title(f'Heatmap of {matrix} correlation matrix')
    plt.savefig(filename)  # Save the figure as a file
    plt.close()  # Close the plot to free up memory

def main():
    # Read CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'df_format_data_ZUARI_RIVER.csv')
    df = pd.read_csv(csv_file_path)

    # Replace 'BDL' with NaN
    df.replace('BDL', np.nan, inplace=True)

    # Convert all columns to numeric, forcing non-numeric values to NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Compute the Pearson correlation matrix
    pearson_corr = df.corr(method='pearson').round(2)

    # Generate and save the heatmap
    heatmap_matrix(df, pearson_corr, "backend/public/images/heatmap.png")

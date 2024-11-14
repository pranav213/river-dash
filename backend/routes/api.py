import os
from generate_heatmap import main as generate_heatmap_script  # Import `main` as `generate_heatmap_script`

def generate_heatmap(river):
    # Define the directory where CSV files are located
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    
    # Map river names to CSV file names
    river_files = {
        'MANDOVI RIVER': 'df_format_data_MANDOVI_RIVER.csv',
        'SAL RIVER': 'df_format_data_SAL_RIVER.csv',
        'ZUARI RIVER': 'df_format_data_ZUARI_RIVER.csv'
    }
    
    # Construct the full path to the CSV file
    file_name = river_files.get(river)
    if not file_name:
        raise ValueError(f"No data file found for river: {river}")

    file_path = os.path.join(data_dir, file_name)
    if not os.path.exists(file_path):
        raise ValueError(f"Data file for {river} not found at path: {file_path}")
    
    # Call `generate_heatmap_script` with the CSV file path
    generate_heatmap_script(file_path)
    return 'backend/public/images/heatmap.png'

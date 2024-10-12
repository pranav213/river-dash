from generate_heatmap import main as generate_heatmap_script

# Function to generate the heatmap
def generate_heatmap():
    generate_heatmap_script()  # Call the script to generate the heatmap
    return 'backend/public/images/heatmap.png'

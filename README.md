# River-Dash

**River-Dash** is a web-based application designed for monitoring river data and visualizing correlation heatmaps for selected rivers. The project consists of a **Flask backend** for data processing and a **React frontend** for user interaction.

---

## Features

- **Dropdown for River Selection**: Choose from multiple rivers (Mandovi, Sal, Zuari).
- **Dynamic Heatmap Generation**: Generates correlation heatmaps for the selected river based on CSV data.
- **Interactive Frontend**: User-friendly interface built with React.

---

## Project Structure

```plaintext
river-dash/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── routes/
│   │   └── api.py             # API routes for heatmap generation
│   ├── generate_heatmap.py    # Script to generate heatmaps
│   ├── data/                  # Folder containing CSV files for river data
│   │   ├── df_format_data_ZUARI_RIVER.csv
│   │   ├── df format data_MANDOVI RIVER.csv
│   │   └── df format data_SAL RIVER.csv
│   ├── public/
│   │   └── images/            # Folder to store generated heatmaps
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/        # React components (Dropdown, Heatmap)
│   │   ├── App.js             # Main React component
│   │   └── index.js           # Entry point for React app
│   └── package.json           # Frontend dependencies
└── README.md                  # Project documentation


Prerequisites

Python (3.8 or higher)
Node.js (16 or higher) and npm
Installation and Setup

Backend (Flask)
Navigate to the backend folder:
cd backend
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
Mac/Linux:
source venv/bin/activate
Windows:
.\venv\Scripts\activate
Install backend dependencies:
pip install -r requirements.txt
Verify the data/ folder contains the required CSV files:
df_format_data_ZUARI_RIVER.csv
df format data_MANDOVI RIVER.csv
df format data_SAL RIVER.csv
Frontend (React)
Navigate to the frontend folder:
cd ../frontend
Install frontend dependencies:
npm install
Running the Project

Step 1: Start the Backend (Flask)
Navigate to the backend directory (if not already there):
cd backend
Activate the virtual environment:
Mac/Linux:
source venv/bin/activate
Windows:
.\venv\Scripts\activate
Start the Flask server:
python app.py
The backend will run on http://localhost:3001.
Step 2: Start the Frontend (React)
Open a new terminal and navigate to the frontend directory:
cd frontend
Start the React development server:
npm start
The frontend will run on http://localhost:3000.
Using the Application

Open http://localhost:3000 in your browser.
Select a river from the dropdown menu.
The application will:
Send a request to the backend (http://localhost:3001/generate-heatmap?river=<RIVER_NAME>).
Generate a heatmap based on the selected river's data.
Display the heatmap in the browser.

Stop the Backend Server: Press CTRL+C in the terminal running python app.py.
Stop the Frontend Server: Press CTRL+C in the terminal running npm start.

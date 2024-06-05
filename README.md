# FastAPI Forecast Download Service

This FastAPI application allows users to download forecasted sensor data in CSV format. The forecast is generated using the Prophet library, and users can specify the request ID and sensor ID to generate and download the forecast.

## Features

- Generate forecast for specified sensor data.
- Download forecasted data as a CSV file.
- Specify request ID and sensor ID for custom downloads.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas
- prophet

## Setup

1. **Clone the repository:**

```sh
git clone https://github.com/chandanlal92/forecast-sensor-data.git
cd forecast-sensor-data
```
2. **Create Virtual enviroment:**
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
3. **Install the required packages:**

```sh
Code kopieren
pip install fastapi uvicorn pandas prophet
```
4. Running the Application

```sh
uvicorn main:app --reload
```
# Usage
```sh
http://127.0.0.1:8000/download_forecast?sensor_id=BT_1011&sensor_id=acc_x
```
This will generate the forecast for the acc_x sensor data and return a downloadable CSV file named BT_1001_acc_x_forecast.csv.

# Author

Chandanlal
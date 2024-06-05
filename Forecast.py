from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
from prophet import Prophet
import os
from datetime import datetime 
app = FastAPI()



# Genarate Forecast of the data
def generate_forecast(sensor_data: pd.Series, periods: int = 10) -> pd.DataFrame:
    df_prophet = pd.DataFrame({
        'ds': pd.date_range(start='2024-01-01', periods=len(sensor_data), freq='D'),
        'y': sensor_data
    })
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# Get request to download forecast of Sensor id and parameter required
@app.get("/download_forecast")
def download_forecast(sensor_id: str = Query(..., description="Sensor ID"), parameter: str = Query(..., description="parameter")):
    filename = f'{sensor_id}.csv'
    parameter=f'{parameter}'
    print(filename)
    df=pd.read_csv(filename)
    forecast = generate_forecast(df[parameter])
    try:
        forecast.to_csv(filename+"_forecasted", index=False)
    
        return FileResponse(path=filename, media_type='text/csv', filename=filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import boto3
import io

s3_bucket = "databricks-project-s3-846372"
s3_key = "models/xgb_model.joblib" 

s3 = boto3.client("s3")
obj = s3.get_object(Bucket=s3_bucket, Key=s3_key)
model_bytes = obj['Body'].read()
xgb_model = joblib.load(io.BytesIO(model_bytes))

# Input data schema
class InputRow(BaseModel):
    vendor_id: int
    passenger_count: int
    trip_distance: float
    payment_type: int
    temperature: int
    dewpoint: int
    humidity: int
    visibilityMiles: int
    windspeedmph: int
    cloudcover: int
    winddirdegrees: int
    sealevel_pressure: float
    psg_per_mile: float
    weather_normal: int
    weather_snow: int
    weather_fog: int
    weather_rain: int

app = FastAPI()

@app.post("/predict")
def predict(data: List[InputRow]):
    try:
        # Convert to list of lists for model input, matching the schema order
        input_list = [
            [
                row.vendor_id,
                row.passenger_count,
                row.trip_distance,
                row.payment_type,
                row.temperature,
                row.dewpoint,
                row.humidity,
                row.visibilityMiles,
                row.windspeedmph,
                row.cloudcover,
                row.winddirdegrees,
                row.sealevel_pressure,
                row.psg_per_mile,
                row.weather_normal,
                row.weather_snow,
                row.weather_fog,
                row.weather_rain
            ]
            for row in data
        ]
        input_array = np.array(input_list)

        # Predict
        results = xgb_model.predict(input_array)

        return {"predictions": results.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

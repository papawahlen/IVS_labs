from datetime import datetime
from pydantic import BaseModel
from app.entities.base_data import AccelerometerData,GpsData

class AgentData(BaseModel):
    accelerometer: AccelerometerData
    gps: GpsData
    timestamp: datetime

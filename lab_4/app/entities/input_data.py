from datetime import datetime
from pydantic import BaseModel, field_validator
from app.entities.base_data import AccelerometerData, GpsData, GroundClearanceData

class InputData(BaseModel):
    accelerometer: AccelerometerData
    gps: GpsData
    ground_clearance: GroundClearanceData
    timestamp: datetime

    @classmethod
    @field_validator("timestamp", mode="before")
    def parse_timestamp(cls, value):
        # Convert the timestamp to a datetime object
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(value)
        except (TypeError, ValueError):
            raise ValueError(
                "Invalid timestamp format. Expected ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)."
            )

import sys
from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.aggregated_data import AggregatedData
import config
from typing import List

from domain.parking import Parking


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
        parking_filename: str
    ) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.accelerometer_data = None
        self.gps_data = None
        self.count = 0
        self.parking_filename=parking_filename
        self.parking_data = None
        pass

    def startReading(self, *args, **kwargs):

        accelerometer_file = open(self.accelerometer_filename)
        self.accelerometer_data = reader(accelerometer_file)
        next(self.accelerometer_data)

        gcp_file = open(self.gps_filename)
        self.gps_data = reader(gcp_file)
        next(self.gps_data)

        parking_file = open(self.parking_filename)
        self.parking_data = reader(parking_file)
        next(self.parking_data)

    def read(self) -> List[AggregatedData]:

        accelerometer_row = next(self.accelerometer_data)
        gps_row = next(self.gps_data)
        parking_row = next(self.parking_data)
        data = AggregatedData(
            Accelerometer(int(accelerometer_row[0]), int(accelerometer_row[1]), int(accelerometer_row[2])),
            Gps(float(gps_row[0]), float(gps_row[1])),
            Parking(int(parking_row[0]), Gps(float(parking_row[1]), float(parking_row[2]))),
            datetime.now(),
            config.USER_ID)
        self.count += 1
        if self.count == 40:
            print("END")
            sys.exit()
        return data


    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
      #  .close()
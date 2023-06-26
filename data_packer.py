# import struct
import json
from datetime import datetime

class DataPacker():
    def __init__(self, id, temp, hum, alt, pres):
        # setting variables 
        # The : float annotation indicates that the temp variable is expected to be a float
        self.id: str = id
        self.temp: float = temp
        self.hum: float = hum
        self.alt: float = alt
        self.pres: float = pres
        self.time_stamp: str = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")

    def make_json(self) -> str:
        data: dict = {}
        data["id"] = self.id
        data["temp"] = self.temp
        data["hum"] = self.hum
        #optional stuff
        # data["alt"] = self.alt
        # data["pres"] = self.pres
        data["time_stamp"] = self.time_stamp
        json_data = json.dumps(data)
        return json_data
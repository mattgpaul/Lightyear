# Parse queries for InfluxDB from user

from database_client import LightyearDBClient
import pandas as pd
from datetime import datetime

TOKEN = 'xEzJEcKhC1R97_D6P-hHkNnXeTZkgiG8PXLwEM-v7exYs3aiLupsKGzpGyzvxN9OFSHwmvYSPJsGIgU0Hf8p0A=='
ORG = 'BartonAerospace'
BUCKET = 'PC Telemetry'
URL = "http://localhost:8086"

client = LightyearDBClient(token=TOKEN, org=ORG, bucket=BUCKET, url=URL)

query_string = """
from(bucket: "PC Telemetry")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] == "CPU_TEST02")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
"""

    
result = client._query_api.query_data_frame(org="BartonAerospace", query=query_string).drop(columns=['result','table','_start','_stop']).set_index('_time')
        
print(result)

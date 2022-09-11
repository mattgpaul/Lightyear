
from database_client import LightyearDBclient
import psutil
from datetime import datetime
from pprint import pprint

TOKEN = 'xEzJEcKhC1R97_D6P-hHkNnXeTZkgiG8PXLwEM-v7exYs3aiLupsKGzpGyzvxN9OFSHwmvYSPJsGIgU0Hf8p0A=='
ORG = 'BartonAerospace'
BUCKET = 'PC Telemetry'
URL = "http://localhost:8086"

client = LightyearDBclient(token=TOKEN, org=ORG, bucket=BUCKET, url=URL)

loop=True
while loop:
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    freq = psutil.cpu_freq(percpu=True)
    stamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    data = [{
        "measurement": "CPU_TEST01",
        "tags":{"CPU_NUM":"CPU0"},
        "fields":{
            "percent":cpu[0],
            "frequency":freq[0][0]
        },
        "time": stamp
    },
    {
        "measurement": "CPU_TEST01",
        "tags":{"CPU_NUM":"CPU1"},
        "fields":{
            "percent":cpu[1],
            "frequency":freq[1][0]
        },
        "time": stamp
    }
    ]
    
    client.WriteData(data)

    

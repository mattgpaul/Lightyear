from database_client import LightyearDBClient
import psutil
from datetime import datetime

TOKEN = 'xEzJEcKhC1R97_D6P-hHkNnXeTZkgiG8PXLwEM-v7exYs3aiLupsKGzpGyzvxN9OFSHwmvYSPJsGIgU0Hf8p0A=='
ORG = 'BartonAerospace'
BUCKET = 'PC Telemetry'
URL = "http://localhost:8086"

client = LightyearDBClient(token=TOKEN, org=ORG, bucket=BUCKET, url=URL)

loop=True
while loop:
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    freq = psutil.cpu_freq(percpu=True)
    stamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    data=[]
    for i, unit in enumerate(cpu):
        data.append({
            "measurement": "CPU_TEST02",
            "tags":{"CPU_NUM":"CPU{}".format(i)},
            "fields":{
                "percent":cpu[i],
                "frequency":freq[i][0]
            },
            "time": stamp
        }
        )
    
    client.WriteData(data)

    
print(data)
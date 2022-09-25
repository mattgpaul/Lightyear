"""Test functionality of the DataStream class"""

import psutil
from lightyear.datastream import DataStream

def CPU_percent():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    return cpu_percent

def CPU_frequency():
    cpu_freq = psutil.cpu_freq(percpu=True)
    return cpu_freq
import psutil
from lightyear.database_client import *

print(psutil.cpu_percent(interval=1))



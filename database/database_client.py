"""
Class to handle InfluxDB functions
"""

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

class LightyearDBclient(object):
    def __init__(self, token, org, bucket, url):
        self._org = org
        self._bucket = bucket
        self._url = url
        self._client = InfluxDBClient(url=url, token=token)
        self._write_api = self._client.write_api()

    def WriteData(self, data):
        self._write_api.write(
            bucket=self._bucket,
            org=self._org,
            record=data
        )
        

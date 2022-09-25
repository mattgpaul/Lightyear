"""Node Dataclass"""

from dataclasses import dataclass

@dataclass
class Node:
    """Parent class for command/telemetry endpoints"""
    name: str
    tags: dict
    mapping_tag: str
  
def ParseData(self):
    pass

def GetData(self):
    pass

def ManageThread(self):
    pass


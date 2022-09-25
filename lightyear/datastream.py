"""Generic datastream. Child class of 'Node'"""

from lightyear.node import Node
from dataclasses import dataclass

@dataclass
class DataStream(Node):
    """Generic stream data class to gather data from a user source"""
    fields: dict
    
    def do_something(self):
        pass
    




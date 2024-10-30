from dnalib.utils import TableUtils, Utils
from dnalib.log import *

class DDL:    

    def __init__(self, layer):
        self.layer = layer.strip().lower()    

class TableDDL(DDL):

    def __init__(self, layer):
        super().__init__(layer)              

    def describe(self):
        raise NotImplementedError("Method describe() must be implemented.")    

    def create_table(self):
        raise NotImplementedError("Method create_table() must be implemented.")    

    def create_view(self):
        raise NotImplementedError("Method create_view() must be implemented.")    
        
    def drop(self):
        raise NotImplementedError("Method drop() must be implemented.")        

    def table_exists(self):
        raise NotImplementedError("Method table_exists() must be implemented.")        



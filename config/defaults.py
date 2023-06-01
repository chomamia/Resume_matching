from .config_node import ConfigNode
import os
path_root = os.getcwd()

config = ConfigNode()
# connect database
config.database = ConfigNode()
config.database.username = 'root'
config.database.password = '01632493915Aa-'
config.database.host = 'localhost'
config.database.nameDB = 'mydb'
config.database.port = '3306'

def get_default_config():
    return config.clone()
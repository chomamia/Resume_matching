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

config.openai = ConfigNode()
config.openai.api_key = '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'

config.save_data = ConfigNode()
config.save_data.resume = 'static/input/resume'
config.save_data.job = 'static/input/job'

def get_default_config():
    return config.clone()
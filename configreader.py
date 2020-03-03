import configparser

config = configparser.ConfigParser()
config.read('config.ini')

FILENAME = config.get('GLOBAL', 'FILENAME')
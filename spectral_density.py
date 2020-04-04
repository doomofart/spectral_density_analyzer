import configparser
import builder as bld
config = configparser.ConfigParser()
config.read('config.ini')

for section in config.sections():
    bld.ExcelBuilder(section)

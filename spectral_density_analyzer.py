import configparser
import builder as bld

cfg = configparser.ConfigParser()
cfg.read('config.ini')

for section in cfg.sections():
    result = bld.ExcelBuilder(cfg, section)
    result.write_output()

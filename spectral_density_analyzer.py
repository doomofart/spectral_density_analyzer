import configparser
import builder as bld
from threading import Thread


def build_output(config, section):
    result = bld.ExcelBuilder(config, section)
    result.write_output()


cfg = configparser.ConfigParser()
cfg.read('config.ini')

for sec in cfg.sections():
    th = Thread(target=build_output, args=(cfg, sec))
    th.start()

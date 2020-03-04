import logging
import sys

logging.basicConfig(level=logging.ERROR)


def value_error(section):
    logging.error('config.ini:Incorrect value in %s section.'
                  '\nProgram has stopped.\nPlease check that value is 1 or 0.' % section)
    sys.exit()

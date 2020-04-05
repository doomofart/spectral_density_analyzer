import logging
import sys

logging.basicConfig(level=logging.ERROR)


def value_error(section, field):
    logging.error('config.ini:Incorrect value in %s section.'
                  '\nProgram has stopped.\nPlease check that value in %s is 1 or 0.' % section, field)
    sys.exit()

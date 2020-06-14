import configparser
import sys

mode = sys.argv[1]

config_path = "config\\config.ini"

config = configparser.ConfigParser()
with open(config_path, 'w') as configfile:
    config._write_section(configfile, "DEFAULT", "RECOGNITION_MODE", mode)
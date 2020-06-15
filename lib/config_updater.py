import configparser
import sys

mode = sys.argv[1]

config_path = "..\\config\\config.ini"

config = configparser.ConfigParser()
config.read(config_path)
config["DEFAULT"]["RECOGNITION_MODE"] = mode

with open(config_path, 'w') as configfile:
    config.write(configfile)
import configparser
import sys

gesture_phrase_map = sys.argv[1]

config_path = "..\\config\\config.ini"

config = configparser.ConfigParser()
config.read(config_path)
config[gesture_phrase_map[0]]["EMERGENCY_MODE"] = gesture_phrase_map[1]

with open(config_path, 'w') as configfile:
    config.write(configfile)
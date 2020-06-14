import configparser
import sys

gesture_phrase_map = sys.argv[1].split(",")

config_path = "config\\config.ini"

config = configparser.ConfigParser()
with open(config_path, 'w') as configfile:
    config._write_section(configfile, gesture_phrase_map[0], "EMERGENCY_MODE", gesture_phrase_map[1])
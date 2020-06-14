import csv
import pyttsx3
from enum import Enum
import os
import configparser

class RecognitionMode(Enum):
    CHARACTER_RECOGNITION_MODE = "To recognize a character at a time"
    EMERGENCY_MODE = "To identify the gesture and select an emergency phrase"

class GestureRecognizer:
    def __init__(self):
        self.decrypted_message = ""
        self.mode = RecognitionMode.CHARACTER_RECOGNITION_MODE.name
        self.config = configparser.ConfigParser()

    def __get_phrase_for_gesture__(self, gesture: int) -> str:
        if gesture != 14:
            self.config.read("config\\config.ini")
            return self.config[f"{gesture}"][self.mode]
        else:
            return None

    def __current_recognition_mode__(self):
        """
        Get the current recognition mode
        P.S - This can be updated via .config_updater.py. So reading always to check in case the mode has changed
        """
        self.config.read("config\\config.ini")
        self.mode = self.config["DEFAULT"]["RECOGNITION_MODE"]

    def __modify_recognized_phrase__(self, recognized_phrase: str):
        """
        This function decides which phrase to be added to the string for the selected gesture
        """
        self.decrypted_message += recognized_phrase

    def gesture_action(self, gesture: int):
        """
        This is the core function which decides on what to do with the recognized gesture
        """
        self.__current_recognition_mode__()
        recognized_phrase = self.__get_phrase_for_gesture__(gesture)
        if recognized_phrase is not None:
            self.__modify_recognized_phrase__(recognized_phrase)

        if (self.mode == RecognitionMode.EMERGENCY_MODE.name and gesture != 14) or (gesture == 14 and self.mode != RecognitionMode.EMERGENCY_MODE):
            engine = pyttsx3.init()
            engine.say(self.decrypted_message)
            engine.runAndWait()
            self.decrypted_message = ""
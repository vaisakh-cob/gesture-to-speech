from serial import Serial
import time
import os
from lib.commands import *
from lib.gesture_to_speech import GestureRecognizer, RecognitionMode
from lib.trainer import train_gesture_recognition_model

def perform_gesture_action(predicted_gesture: []):
     """
     This function performs the actions based on the predicted gesture
     """
     gesture = predicted_gesture[0]
     gesture_recognizer.gesture_action(gesture)

def run_recognizer():
     """
     This function keeps receiving the input from the Serial connection with the Arduino
     """
     while True:
          arduino_input_pattern = ser.readline()
          arduino_input_string = arduino_input_pattern[:(len(arduino_input_pattern)-2)].decode()
          pattern_split = arduino_input_string.split(',')
          
          pattern_listData = [float(x) for x in pattern_split]
          pattern_predict = lin_svc_pattern.predict([pattern_listData])

          perform_gesture_action(pattern_predict)
          

lin_svc_pattern = train_gesture_recognition_model()
gesture_recognizer = GestureRecognizer()

ser = Serial('/dev/ttyACM0')
if ser.isOpen() == False:
     ser.open()

time.sleep(1)

run_recognizer()
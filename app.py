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
     # Performs the actions. Uses the already created gesture_recognizer object
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
          # Used the trained model to predict which gesture was shown
          pattern_predict = lin_svc_pattern.predict([pattern_listData])
          # To perform whichever actions is relevant to the gesture
          perform_gesture_action(pattern_predict)
          

# This calls trainer.py and invokes the train gesture model function. Used to train the model
lin_svc_pattern = train_gesture_recognition_model()
# Creates an object for the Gesture Recognizer, which is the core logic for performing any action
gesture_recognizer = GestureRecognizer()

# Connects to a particular Arduino Serial PORT
# Checks if the connection is open.
# If not, opens the connection
ser = Serial('/dev/ttyACM0')
if ser.isOpen() == False:
     ser.open()

time.sleep(1)

# Starts receiving the signals from Arduino Serial connection. Calls the run_recognizer function
run_recognizer()
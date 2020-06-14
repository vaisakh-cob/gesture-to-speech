from aenum import MultiValueEnum
from lib.smsHelper import Sms4India

class ACTIONS(MultiValueEnum):
    LightOff="turn off the light", "turn the light off"
    LightOn="turn on the light"
    Call="call"
    Message="message"
    DoorClose="close the door", "close door"
    DoorOpen="open the door"

PEOPLE = {
    "vivek": "",
    "vaisakh": "",
    "sherin": "9562733462"
}

def CheckForEmergencyPhrase(main_string: str) -> bool:
    """
    This function checks if the input string contains any of the pre=defined Emergency Phrases
    """
    try:
        action = ACTIONS(main_string.lower()).name
        return Command().perform_action(action, main_string.lower())
    except:
        return False
        
class Command():
    def perform_action(self, action: ACTIONS, message: str):
        """
        This function performs the action in case we find any emergency phrase
        """
        if (action == ACTIONS.LightOff.name):
            print(ACTIONS.LightOff.value)
        
        elif (action == ACTIONS.LightOn.name):
            print(ACTIONS.LightOn.value)
        
        elif (action == ACTIONS.DoorClose.name):
            print(ACTIONS.DoorClose.value)
        
        elif (action == ACTIONS.DoorOpen.name):
            print(ACTIONS.DoorOpen.value)
                
        else:
            recipient = PEOPLE[message.replace(' ', '').replace(action.lower(), '')]
            
            if (action == ACTIONS.Call.name):
                self.Call(recipient)
            elif (action == ACTIONS.Message.name):
                self.Message(recipient, message)
        
        return True

    def Call(self, recipient):
        """
        This function calls the recipient if the emergency phrase was to call
        Not supported in V 1.0.0
        """
        print("Call is not supported right as of now")

    def Message(self, recipient, message):
        """
        This function messages the recipient if the emergency phrase was to message
        Very basic implementation and only works if the string contains "Message" and the recipient name
        TODO: Make implementation for this better
        """
        print(recipient + " Hi")
        Sms4India("THHJS0FCSDYZI39HMD90UYC2GIU2OREM", "XJPMW1RJ7MF9YWWJ").sendPostRequest(recipient, "This is an emergency")
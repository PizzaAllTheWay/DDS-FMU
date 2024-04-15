"""
    NOTE: BEFORE RUNNING THIS CODE, Run the ./compile_fmu.sh to make sure you have the latest data structure the DDS-FMU is sending data with
"""



# Python Libraries
import time
import math
import struct
from dataclasses import dataclass, field, fields

# DDS Libraries
from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
from cyclonedds.idl import IdlStruct
from cyclonedds.util import duration

# IDL Data Structure Library




# DDS Topic Setup (START) --------------------------------------------------
@dataclass
class MyCustomSignalStructureOutput(IdlStruct, typename="idl::MyCustomSignalStructureOutput"):
    my_state: bool
    # my_value: int # Assuming uint16 maps to int in Python
    # my_percentage: float
    # my_letter: str # Assuming char maps to a single character string in Python
    # my_text: str

# Create a DomainParticipant
# This way this python script is bounded to DDS
# We can set many parameters here to configure out relationship between Python script and DDS, like Domain ID, QoS, Listeners ect...
# For our usage we simply leave parameters as default, nothing to set up basically
dp = DomainParticipant()

# This is Where we define topics and what type of data structure they have
topicInput = Topic(dp, "MyCustomDDSFMUTopicInput", MyCustomSignalStructureInput)
topicOutput = Topic(dp, "MyCustomDDSFMUTopicOutput", MyCustomSignalStructureOutput)

# We now finally bind these topics to DDS with correct data structure
# This is the objects we will use to read or write to our DDS-FMU on STC
dr = DataReader(dp, topicInput)
dw = DataWriter(dp, topicOutput)
# DDS Topic Setup (STOP) --------------------------------------------------



# DDS Functions (START) --------------------------------------------------
# Function to read data from DDS
def read_data_bool() -> bool:
    # Read value from DDS-FMU
    msg = dr.read()

    # Check that the message is not empty and that DDS-FMU actually published something
    if msg:
        # Message is a array, and inside the array we find our data structure with aropriate data
        data = msg[0].fmu_output_value

        return data
    else:
        print("ERROR: Failed to retrieve data from DDS-FMU :(")
        return None
    
def read_data_int(dr):
    try:
        messages = dr.take()
        for message in messages:
            if message.sample_info.valid_data:
                data = MyCustomSignalStructureInput.deserialize(message.data)
                print(f"Received: {data.value}")
            else:
                print("Received invalid data.")
    except:
        pass

def read_data():
    # Read value from DDS-FMU
    msg = dr.read()
    print(msg)

    # Check that the message is not empty and that DDS-FMU actually published something
    if msg:
        # Message is a array, and inside the array we find our data structure with aropriate data
        data = msg[0].fmu_output_value
        
        print(data)
        return data
    else:
        print("ERROR: Failed to retrieve data from DDS-FMU :(")
        return None
    
# Function to publish data to DDS
def publish_data(state:bool, value: int, percentage: float, letter: str, text: str) -> None:
    # Construct the message with the correct data type and values inside to publish to DDS, so that DDS FMU can receive it and output it 
    msg = MyCustomSignalStructureOutput(
        my_state = state,
        # my_value = value,
        # my_percentage = percentage,
        # my_letter = letter,
        # my_text = text
        )

    # Send message to DDS for DDS-FMU to receive as an output
    dw.write(msg)
# DDS Functions (STOP) --------------------------------------------------



# Mail loop (START) --------------------------------------------------
# Variables for DDS Writing
state = True
value = 0
percentage = 420.69
letter = 'W'
text = "Hello World :D"

# Variables for DDS Reading
data = 0

# Variable for DDS communication
waitPeriod = 1

# Variables that change over time
variableChanging = 0.0

if __name__ == "__main__":
    try:
        while True:
            # Simulate value change
            variableChanging += 0.1
            value = int(abs(10 * math.sin(variableChanging)))

            # Communicate with DDS-FMU
            data = read_data()
            publish_data(state, value, percentage, letter, text)
            
            # Debugging
            print(f"DATA RECEIVED: data = {data}")
            print(f"DATA SENT    : state = {state}, value = {value}, percentage = {percentage}, letter = {letter}, text = {text}")
            
            # A small timeout in order to not overwhelm DDS writer and reader nodes
            time.sleep(waitPeriod)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
# Mail loop (STOP) --------------------------------------------------
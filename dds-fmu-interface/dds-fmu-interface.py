from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
from cyclonedds.qos import Policy, Qos
from cyclonedds.idl import IdlStruct, types
from cyclonedds.util import duration
from cyclonedds.core import Listener

# Assuming the 'MyCustomSignalStructure' class is generated and available from your IDL file
@dataclass
class MyCustomSignalStructure(IdlStruct, typename="idl::MyCustomSignalStructure"):
    my_state: bool
    # my_value: int  # Assuming uint16 maps to int in Python
    # my_percentage: float
    # my_letter: str  # Assuming char maps to a single character string in Python
    # my_text: str

# Create a DomainParticipant
dp = DomainParticipant()

# Create a Topic without explicitly setting QoS here; adjust as necessary based on available methods
tpOutput = Topic(dp, "MyCustomDDSFMUTopicOutput", MyCustomSignalStructure)
tpInput = Topic(dp, "MyCustomDDSFMUTopicInput", MyCustomSignalStructure)

# Create a DataWriter and DataReader without explicitly setting QoS; see below for adjustment
dw = DataWriter(dp, tpOutput)
dr = DataReader(dp, tpInput)

# Function to publish data
pub_state = True
def publish_data():
    global pub_state
    pub_state = not pub_state
    # sample = MyCustomSignalStructure(my_state=True, my_value=12345, my_percentage=99.9, my_letter='A', my_text="Hello DDS World!")
    sample = MyCustomSignalStructure(my_state=pub_state)
    dw.write(sample)
    print(f"Data published. {pub_state}")

# Function to read data
def read_data():
    received_samples = dr.read()
    if received_samples:
        for sample in received_samples:
            # print(f"Received data - State: {sample.my_state}, Value: {sample.my_value}, Percentage: {sample.my_percentage}, Letter: {sample.my_letter}, Text: {sample.my_text}")
            print(f"Received data - State: {sample.my_state}")

if __name__ == "__main__":
    import time
    try:
        while True:
            publish_data()
            time.sleep(1)  # Adjust timing as needed
            read_data()
            time.sleep(1)  # Adjust timing as needed
    except KeyboardInterrupt:
        print("Program interrupted by user.")

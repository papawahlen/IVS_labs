from app.entities.input_data import InputData
from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData
import time


def process_agent_data(input_data: InputData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
    agent_data (AgentData): Agent data that contains accelerometer, GPS, and timestamp.
    Returns:
    processed_data (ProcessedAgentData): Processed data containing the classified state of
    the road surface and agent data.
    """
    state = "incorrectly entered data"
    if 18 <= input_data.ground_clearance.length <= 20:
        state = "good"
    elif 20 < input_data.ground_clearance.length <= 30:
        state = "okay"
    elif input_data.ground_clearance.length > 30:
        state = "bad"
    time.sleep(1)
    return ProcessedAgentData(road_state=state,
                              agent_data=AgentData(accelerometer=input_data.accelerometer,
                                                   gps=input_data.gps,
                                                   timestamp=input_data.timestamp))

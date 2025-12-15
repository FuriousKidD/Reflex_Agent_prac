import random

class SimpleReflexAgentThermostat:
    def __init__(self, ideal_temp = 22):
        self.ideal_temp = ideal_temp
    
    # Sensor
    def percieve(self):
        """ Simulate reading the current temperature from a sensor. 
            In a real-world scenario, this would interface with actual hardware.
        """
        return random.randint(15, 30)  # Simulated temperature reading
    
    # Agent Function
    def condition_action(self, current_temp : int):
        """These are the condition-action rules for the thermostat agent."""
        if current_temp < self.ideal_temp - 2:
            return "Heater On"
        elif current_temp > self.ideal_temp + 2:
            return "AC On"
        else:
            return "Maintain Current State"
    
    # Simulation Loop
    def run(self, steps = 10):
        for step in range(steps):

            # 1. The agent perceives the environment
            temp = self.percieve()

            #2. The agent decides on an action based on its condition-action rules
            action = self.condition_action(temp)

            # 3. The agent performs the action based on the condition-action rules
            print(f"Step {step + 1}: Current Temp = {temp} Degrees Celcius, Action = {action}")

            # TO-DO: Simulate time passing
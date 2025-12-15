import random

class SimpleReflexAgentThermostat:
    def __init__(self, ideal_temp = 22, ideal_humidity = 40):
        self.ideal_temp = ideal_temp
        self.ideal_humidity = ideal_humidity
    
    # Sensor
    def percieve(self):
        """ Simulate reading the current temperature & Humidity from the sensor. 
            In a real-world scenario, this would interface with actual hardware.
        """
        temperature = int(input("Enter current temperature:")) # in Degrees Celcius
        humidity = int(input("Enter current Humidity:")) # in Percentage
        return [temperature, humidity] # Returning as a list simulated [temperature, humidity]
    
    # Agent Function
    def condition_action(self, current_temp : int, current_humidity : int) :
        """These are the condition-action rules for the thermostat agent."""
        # Low Temperature
        if current_temp < self.ideal_temp - 2:
            if current_humidity < self.ideal_humidity - 10: # Low Humidity
                return "Turn on Heator & Humidifier"
            elif current_humidity > self.ideal_humidity + 10: # High Humidity
                return "Turn on Heator & Dehumidifier"
            else:
                return "Turn on Heator"
        # High Temperature
        elif current_temp > self.ideal_temp + 2:
            if current_humidity < self.ideal_humidity - 10: # Low Humidity
                return "Turn on AC & Humidifier"
            elif current_humidity > self.ideal_humidity + 10: # High Humidity
                return "Turn on AC & Dehumidifier"
            else:
                return "Turn on AC"
        else:
            if current_humidity < self.ideal_humidity - 10: # Low Humidity
                return "Turn on Humidifier"
            elif current_humidity > self.ideal_humidity + 10: # High Humidity
                return "Turn on Dehumidifier"
            else:
                return "Maintain Current State"
    
    # Simulation Loop
    def run(self, steps = 10):
        for step in range(steps):

            # 1. The agent perceives the environment
            condition = self.percieve()

            #2. The agent decides on an action based on its condition-action rules
            action = self.condition_action(condition[0], condition[1])

            # 3. The agent performs the action based on the condition-action rules
            print(f"Step {step + 1}: \n Current Temp = {condition[0]} Degrees Celcius \n Current Humidity = {condition[1]}% \n Action = {action}")

            # TO-DO: Simulate time passing
    
    @property
    def ideal_conditions(self):
        self.ideal_temp = int(input("Enter ideal temperature:")) # in Degrees Celcius
        self.ideal_humidity = int(input("Enter ideal Humidity:")) # in Percentage
        return (self.ideal_temp, self.ideal_humidity)
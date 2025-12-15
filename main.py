from thermostat_agent import SimpleReflexAgentThermostat

def main():
    agent = SimpleReflexAgentThermostat(ideal_temp=22, ideal_humidity=40)
    agent.ideal_conditions  # Prompt user to set ideal conditions
    agent.run(steps=1)

if __name__ == "__main__":
    main()
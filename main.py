from thermostat_agent import SimpleReflexAgentThermostat

def main():
    agent = SimpleReflexAgentThermostat(ideal_temp=22, ideal_humidity=40)
    agent.run(steps=5)

if __name__ == "__main__":
    main()
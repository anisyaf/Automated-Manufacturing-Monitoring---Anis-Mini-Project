import pandas as pd
import numpy as np
import random

num_records = 1000
machines = ["Die Bonder", "Wafer Bumper", "Inspection"]
shifts = ["Morning", "Evening", "Night"]

data = []

for i in range(num_records):
    shift = random.choice(shifts)
    temperature = round(np.random.normal(75, 5), 2)
    
    defects = random.randint(0, 10)

    if shift == 'Night':
        defects += 1
        
    if temperature > 80:
        defects += random.randint(1, 3)

    defects = min(defects, 20)

    downtime = round(np.random.normal(5, 2), 1)
    downtime = max(downtime, 0)

    anomaly_chance = 0.05

    if random.random() < anomaly_chance:
        anomaly_type = random.choice(["Temperature", "Defects", "Downtime", "Combined"])
        if anomaly_type == "Temperature":
            temperature += random.randint(10, 20)
        elif anomaly_type == "Defects":
            defects += random.randint(3, 7)
        elif anomaly_type == "Downtime":
            downtime += random.randint(5, 15)
        elif anomaly_type == "Combined":
            temperature += random.randint(10, 20)
            defects += random.randint(3, 7)
            downtime += random.randint(5, 15)
        
    defects = min(defects, 25)
    downtime = min(downtime, 30)
    temperature = min(temperature, 120)
    
    record = {
        "Machine": random.choice(machines),
        "Shift": shift,
        "Temperature": temperature,
        "Pressure": round(np.random.normal(1.0, 0.1), 3),
        "Time": random.randint(20, 60),
        "Output": random.randint(80, 120), 
        "Defects": defects, 
        "Downtime": downtime
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("data/simulated_factory_data.csv", index=False)

print("the job is done")
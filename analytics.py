import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("data/simulated_factory_data.csv")

# Basic Analytics

print("Data loaded. Shape:", df.shape)
print(df.head())

print ("\n Summary")
print(df.describe())

machine_summary = df.groupby("Machine")[["Output","Defects","Downtime"]].mean()
print("\n Average Performance by Machine ")
print(machine_summary)

shift_summary = df.groupby("Shift")[["Output","Defects","Downtime"]].mean()
print("\n Average Performance by Shift")
print(shift_summary)

anomalies = df[
    (df["Temperature"] > 90) | 
    (df["Defects"] > 15) |
    (df["Downtime"] > 20 )
]

print("\n Anomalies Detected ")
print(anomalies)

anomalies.to_csv("data/anomalies.csv", index=False)
machine_summary.to_csv("data/machine_summary.csv")
shift_summary.to_csv("data/shift_summary.csv")

# Visual Analytics 

# 1. Average Output by Machine 
plt.figure(figsize= (10, 6))
df.groupby("Machine")["Output"].mean().plot(kind="bar", color= "skyblue")
plt.title("Average Output by Machine")
plt.ylabel("Output")
plt.savefig("data/output_by_machine.png")
plt.show()

# 2. Average Defects by Shift 
plt.figure(figsize= (10,6))
df.groupby("Shift")["Defects"].mean().plot(kind="bar", color= "purple")
plt.ylabel("Defects")
plt.savefig("data/defects_by_shift.png")
plt.show()

# 3. Output vs Defects with anomaly highlight 
plt.figure(figsize= (10,6))
plt.scatter(df["Output"], df["Defects"], alpha=0.5, c="blue", label="Normal Data")
plt.scatter(anomalies["Output"], anomalies["Defects"], alpha=0.9, c="red", label="Anomalies")
plt.title("Output vs Defects (Anomalies Highlighted)")
plt.xlabel("Output")
plt.ylabel("Defects")
plt.legend
plt.savefig("data/output_vs_defects_anomalies.png")
plt.show()

# 4. Temperature Distribution with Anomalies 
plt.figure(figsize= (10,6))
plt.hist(df["Temperature"], bins= 30, color= "orange", alpha= 0.7, label= "Normal Data")
plt.hist(anomalies["Temperature"], bins=30, color= "red", alpha= 0.7, label= "Anomalies")
plt.title("Temperature Distribution (with anomaly)")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.legend
plt.savefig("data/temperature_distribution_anomalies.png")
plt.show()

print("Plots with anomaly highlights saved!")
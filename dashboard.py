import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt

st.title("Automated Manufacturing Monitoring Dashboard")

df = pd.read_csv("data/simulated_factory_data.csv")

st.subheader("Overall Summary")
st.dataframe(df.describe())

machine_filter = st.multiselect("Select Machine(s)", df["Machine"].unique(), default=df["Machine"].unique())
filtered_df = df[df["Machine"].isin(machine_filter)]

anomalies = filtered_df[
    (filtered_df["Temperature"] > 90) | 
    (filtered_df["Defects"] > 15) | 
    (filtered_df["Downtime"] > 20)
    ]

st.subheader("Anomalies")

if anomalies.empty:
    st.write("No anomalies detected.")
else:                  
    st.dataframe(anomalies)

# 4.1 Output by Machine
st.subheader("Average Output by Machines")
fig, ax = plt.subplots()
avg_output = filtered_df.groupby("Machine")["Output"].mean()
bars = ax.bar(avg_output.index, avg_output.values, color="blue")
ax.set_ylabel("Average Output")
ax.set_xlabel("Machine")
ax.set_title("Average Output per Machine")
ax.bar_label(bars, fmt="%.5f")
st.pyplot(fig)

st.markdown("**Insight:** The machine with the highest average output contributes most to production. This can help in optimizing machine allocation.")


# 4.2 Defects by Shift
st.subheader("Average Defects by Shifts")
fig2, ax2 = plt.subplots()
avg_defects = filtered_df.groupby("Shift")["Defects"].mean()
bars2 = ax2.bar(avg_defects.index, avg_defects.values, color="orange")
ax2.set_ylabel("Average Defects")
ax2.set_xlabel("Shift")
ax2.set_title("Average Defects per Shift")
ax2.bar_label(bars2, fmt="%.5f")
st.pyplot(fig2)

st.markdown("**Insight:** This highlights if defect rates spike in certain shifts, like the night shifts, so corrective actions can be planned.")


# 4.3 Defect Rate (%) by Machine
st.subheader("Defect Rate by Machine")
fig3, ax3 = plt.subplots()
avg_defect_rate = (filtered_df["Defects"] / filtered_df["Output"]).groupby(filtered_df["Machine"]).mean()
bars3 = ax3.bar(avg_defect_rate.index, avg_defect_rate.values, color="purple")
ax3.set_ylabel("Average Defect Rate")
ax3.set_xlabel("Machine")
ax3.set_title("Defect Rate by Machine")
ax3.bar_label(bars3, fmt="%.5f")  
st.pyplot(fig3)

st.markdown("**Insight:** Focuses on quality rather than just quantity, showing which machines produce more defects relative to output.")

# 4.4 Downtime Distribution
st.subheader("Downtime Distribution")

bins = [0, 5, 10, 20, 50]  # downtime in minutes
labels = ["Short (0-5 min)", "Medium (5-10 min)", "Long (10-20 min)", "Very Long (20+ min)"]

downtime_cat = pd.cut(filtered_df["Downtime"], bins=bins, labels=labels, include_lowest=True)
downtime_counts = downtime_cat.value_counts().sort_index()

fig4, ax4 = plt.subplots()
bars = ax4.bar(downtime_counts.index, downtime_counts.values, color="salmon", alpha=0.7, edgecolor="black")
ax4.set_xlabel("Downtime Category")
ax4.set_ylabel("Frequency")
ax4.set_title("Downtime Distribution by Category")
ax4.bar_label(bars)
st.pyplot(fig4)

st.markdown("**Insight:** Most downtime events are in the 'Short' or 'Medium' category. Very long downtime events are rare but may need urgent attention.")

# 4.5 Output vs. Defects
st.subheader("Output vs Defects")
fig5, ax5 = plt.subplots()
ax5.scatter(filtered_df["Output"], filtered_df["Defects"], alpha=0.5, label="Normal")
ax5.scatter(anomalies["Output"], anomalies["Defects"], alpha=0.9, color="red", label="Anomaly")
ax5.set_xlabel("Output")
ax5.set_ylabel("Defects")
ax5.set_title("Output vs Defects (Anomalies Highlighted)")
ax5.legend()
st.pyplot(fig5)

st.markdown("**Insight:** Identifies batches where high output correlates with high defects. Red points indicate anomalies needing attention.")

st.subheader("Summary Metrics")

filtered_df_nonzero = filtered_df[filtered_df["Output"] > 0]

total_output = filtered_df["Output"].sum()
avg_defect_rate = (filtered_df_nonzero["Defects"] / filtered_df_nonzero["Output"]).mean()
total_downtime = filtered_df["Downtime"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Output", f"{total_output:.0f} units")
col2.metric("Average Defect Rate", f"{avg_defect_rate:.4f}")
col3.metric("Total Downtime", f"{total_downtime:.2f} min")

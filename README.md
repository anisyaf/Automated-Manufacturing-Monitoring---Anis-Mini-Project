# Interactive Manufacturing Dashboard

**Live Demo:** [Open Streamlit App](https://automated-manufacturing-monitoring-anis-mini-project.streamlit.app/)
**GitHub Repo:** [Link](https://github.com/anisyaf/automated-manufacturing-monitoring---anis-mini-project/blob/main/dashboard.py)

---

## Description

I developed an **interactive dashboard** to simulate and monitor manufacturing processes, focusing on **production output, defect rates, downtime, and anomaly detection**. This project helped me understand how to build Python-based analytics dashboards and visualize complex datasets effectively.

**What I Did:**
What I Did:

* Defined project scope, metrics, and KPIs (output, defects, defect rates, downtime, anomalies).
* Developed scripts to simulate manufacturing data and its analytics
* Designed the dashboard layout and visualizations to make data actionable.
* Implemented interactive filtering, anomaly detection, and categorized visualizations using Streamlit.
* Interpreted data to identify graph trends and quality issues.
* Troubleshot Git Bash and configured Git/GitHub to successfully deploy the app to Streamlit Cloud (my first attempt).
* Practiced Python, Pandas, Matplotlib, and Streamlit, reinforcing data analysis and visualization workflows.

**Impact / Takeaways:**

* Built a working prototype demonstrating **data-driven manufacturing monitoring**.
* Practiced translating complex data into **actionable insights** for operational decision-making.

---

## Process

### Problem Statement

In modern manufacturing, factories must balance output, quality, and uptime. Unexpected machine downtime, high defect rates, or anomalies (like overheating) can significantly impact yield.

**Goal:** Build an **automated monitoring dashboard** to allow engineers to:

* Detect anomalies early (temperature, defects, downtime)
* Compare machine and shift performance
* Track defect rates to improve quality
* Visualize trends for decision-making

---

### Data Description

Simulated **1000 records** of factory data with these fields:

| Column      | Description                                            |
| ----------- | ------------------------------------------------------ |
| Machine     | Type of machine (Die Bonder, Wafer Bumper, Inspection) |
| Shift       | Work shift (Morning, Evening, Night)                   |
| Temperature | Average operating temperature (°C)                     |
| Output      | Units produced in the batch                            |
| Defects     | Units failed quality checks                            |
| Downtime    | Minutes of unplanned downtime                          |

---

### Key Metrics (KPIs)

* **Average Output per Machine**
* **Defects per Shift**
* **Defect Rate (%) = Defects / Output × 100**
* **Downtime Distribution (minutes per event)**
* **Anomalies**:

  * Temperature > 90°C
  * Defects > 15 units
  * Downtime > 20 minutes

---

## Results

* Fully **interactive dashboard** in Streamlit
* Real-time KPI visualizations and anomaly detection
* Easy-to-read charts for **decision-making insights**

---

## Tech Stack

* Python
* Streamlit
* Pandas, Matplotlib, Numpy

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py
```

---

## Behind-This-Project

**Anis Syafiqah**
📧 [wan.anisyafiqah03@gmail.com](mailto:wan.anisyafiqah03@gmail.com)
[LinkedIn](https://www.linkedin.com/in/wananisyafiqah/) | [Portfolio/GitHub](https://github.com/anisyaf)

*"Passion, determination, perseverance."*


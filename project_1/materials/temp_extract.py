import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("./project_1/materials/CDC_DATA.csv")

state = "AZ"
start_date = datetime(2023, 10, 1)
end_date = datetime(2024, 8, 1)

df = df[
    ["state", "date", "total_patients_hospitalized_confirmed_influenza"]
]
df = df[df["state"] == "AZ"]

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

plt.plot(df['date'],df['total_patients_hospitalized_confirmed_influenza'])
plt.show()

df.to_csv('./project_1/materials/AZ_DATA.csv', index = False)
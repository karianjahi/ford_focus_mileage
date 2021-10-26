import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
ford_mileage_file = "mileage.csv"
with open(ford_mileage_file, "r") as f:
    data = f.read()

data_lines = data.split("\n")

item = data_lines[0]

def get_date_and_mileage(item):
    splits = item.split()
    mileage = splits[-1]
    date_pieces = splits[:-1]
    date = ""
    for piece in date_pieces:
        date = date + " " + piece
    date = str(pd.to_datetime(date)).split(" ")[0]
    
    return {"mileage": mileage, "date": date}

dates = []
mileage = []
for item in data_lines:
    dates.append(get_date_and_mileage(item)["date"])
    mileage.append(get_date_and_mileage(item)["mileage"])

df = pd.DataFrame({"date": dates, "mileage": mileage})
df.to_csv("mileage.csv", index=False)


df = pd.read_csv("mileage.csv", index_col=0, parse_dates=True)
df["diff"] = [i for i in df["mileage"].diff()]
df[["diff"]].plot()
plt.show()

    
    
    

import pandas as pd
ford_mileage_file = "/home/karianjahi/ford_focus_mileage_records.txt"
with open(ford_mileage_file, "r") as f:
    data = f.read()

data_lines = data.split("\n")[:-1]

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
df.to_csv("ford_focus/mileage.csv", index=False)

    
    
    

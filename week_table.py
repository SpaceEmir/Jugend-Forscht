import pandas as pd
from asking import gibTage as gT

data = {
    "Name": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
}

tage = gT()

gefuehle = []

for tag in data["Name"]:
    gefuehle.append(tage[tag][0].capitalize())

data["Gefühl"] = gefuehle

df = pd.DataFrame(data)
print(df)
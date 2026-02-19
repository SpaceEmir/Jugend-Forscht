import pandas as pd
from fragen import gibTage as gT

tage = gT()

data = {
    "Tag": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
    "Gefühl": [tage[tag][0].capitalize() for tag in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]]
}

df = pd.DataFrame(data)
print(df)
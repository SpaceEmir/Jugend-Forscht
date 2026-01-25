import gefühl
import pandas as pd

def bin_find(bin):
    return f"((({bin[0]} * 2 + {bin[1]}) * 2 + {bin[2]}) * 2 + {bin[3]}) * 2 + {bin[4]}"

gefuehle = gefühl.g()

data = {
    "Gefühl": [],
    "Binärcode": [],
    "Dezimalzahl (d)": [],
    "Formel (f = 200 + d * 10)": [],
    "Frequenz (Hz)": []
}

for gefuehl, bin in gefuehle.items():
    data["Gefühl"].append(gefuehl.capitalize())
    data["Binärcode"].append(str(bin))
    data["Dezimalzahl (d)"].append(str(f"{int(bin, 2)}{bin_find(bin)}"))
    data["Formel (f = 200 + d * 10)"].append(f"200 + {int(bin, 2)} * 10 = {200 + int(bin, 2) * 10}")
    data["Frequenz (Hz)"].append(gefühl.bin_umwandeln(bin))

df = pd.DataFrame(data)
print(df)
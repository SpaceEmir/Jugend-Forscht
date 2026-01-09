import matplotlib.pyplot as plt
from asking import gibTage as gT

tage = gT()
tage_name = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

gefuehle = []

for tag in tage_name:
    gefuehle.append(tage[tag][0])

numbering = {
    "aufregung": 6,
    "glück": 5,
    "ruhe": 4,
    "traurigkeit": 3,
    "angst": 2,
    "wut": 1
}

gefuehle = list(numbering[gefuehl] for gefuehl in gefuehle)

plt.figure(figsize=(6, 6.5))
plt.bar(tage_name, gefuehle)
plt.yticks([1, 2, 3, 4, 5, 6], ["Wut", "Angst", "Traurigkeit", "Ruhe", "Glück", "Aufreung"])
plt.show()
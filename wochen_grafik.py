import matplotlib.pyplot as plt
from fragen import gibTage as gT

tage = gT()

tag_namen = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag"
]

gefuehl_werte = {
    "traurigkeit": 1,
    "angst": 2,
    "wut": 3,
    "ruhe": 4,
    "glück": 5,
    "aufregung": 6
}

werte = [
    gefuehl_werte[tage[tag][0]]
    for tag in tag_namen
]

plt.figure(figsize=(10, 5))
plt.bar(tag_namen, werte)

plt.yticks(
    [1, 2, 3, 4, 5, 6],
    [
        "Traurigkeit",
        "Angst",
        "Wut",
        "Ruhe",
        "Glück",
        "Aufregung"
    ]
)

plt.title("Meine Gefühle der Woche")
plt.xlabel("Tag")
plt.ylabel("Gefühl")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.show()
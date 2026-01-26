import matplotlib.pyplot as plt

gefuehle = [
    ("Aufregung", 3, 4),
    ("Glück", 3, 0),
    ("Ruhe", 1, -5),
    ("Traurigkeit", -3, -1),
    ("Angst", -2, 3),
    ("Wut", -4, 5)
]

plt.figure()
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xticks(range(-5, 6, 1))
plt.yticks(range(-5, 6, 1))

plt.plot([-5, 5], [0, 0], linewidth=1, color="black")

plt.plot([0, 0], [-5, 5], linewidth=1, color="black")

for gefuehl, x, y in gefuehle:
    plt.scatter(x, y)
    plt.text(x, y + 0.2, gefuehl)

plt.xlabel("negativ/positiv")
plt.ylabel("ruhig/energisch")

plt.grid(True)
plt.show()
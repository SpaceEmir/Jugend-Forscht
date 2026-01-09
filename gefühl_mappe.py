import matplotlib.pyplot as plt

duygular = [
    ("Aufregung", 3, 4),
    ("Glück", 3, 2),
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

for isim, x, y in duygular:
    plt.scatter(x, y)
    plt.text(x, y + 0.2, isim)

plt.xlabel("negativ/positiv")
plt.ylabel("ruhig/energisch")

plt.grid(True)
plt.show()
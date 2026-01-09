import matplotlib.pyplot as plt
from emotion import *

gefuehle = g()
frequenzen = [umwandeln(gefuehl) for gefuehl in gefuehle.keys()]
gefuehle = ["Aufregung", "Glück", "Ruhe", "Traurigkeit", "Angst", "Wut"]

print(gefuehle)
print(frequenzen)

dp = list(zip(gefuehle, frequenzen))
dp.sort(key=lambda x: x[1], reverse=True)
dersler, puanlar = zip(*dp)

plt.figure(figsize=(6, 6.5))
plt.bar(dersler, puanlar)
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
plt.show()
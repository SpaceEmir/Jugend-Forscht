import os
import json
import datetime
from gefühl import g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATEI = os.path.join(BASE_DIR, "gefühle.json")


if os.path.exists(DATEI):
    with open(DATEI, "r", encoding="utf-8") as f:
        tage = json.load(f)
else:
    tage = {
        "Montag": ["", False],
        "Dienstag": ["", False],
        "Mittwoch": ["", False],
        "Donnerstag": ["", False],
        "Freitag": ["", False],
        "Samstag": ["", False],
        "Sonntag": ["", False],
        "last_date": datetime.date.today().isoformat()
    }


def speichere_tage():
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(tage, f, ensure_ascii=False, indent=2)


def main():
    global tage

    heute = datetime.datetime.now()
    heute_datum = datetime.date.today().isoformat()
    tag = heute.strftime("%A")

    english_tage = {
        "Monday": "Montag",
        "Tuesday": "Dienstag",
        "Wednesday": "Mittwoch",
        "Thursday": "Donnerstag",
        "Friday": "Freitag",
        "Saturday": "Samstag",
        "Sunday": "Sonntag"
    }

    tag = english_tage.get(tag, tag)

    if tag == "Montag" and tage.get("last_date") != heute_datum:
        for t in tage:
            if t != "last_date":
                tage[t] = ["", False]

    tage["last_date"] = heute_datum

    gefuehle = g()

    if heute_datum in ["2025-12-24", "2025-12-25", "2026-12-24", "2026-12-25"]:
        print("❄️⛄🎄🎁 Frohe Weihnachten! ❄️⛄🎄🎁")

    if heute_datum in ["2025-12-31", "2026-12-31"]:
        print("🎇 Frohes Silvester! 🎆")

    if heute_datum in ["2026-01-01", "2027-01-01"]:
        print("🕯️ Frohes neues Jahr! 🔔")

    if tage[tag][1]:
        frage = input("Heute hast du dein Gefühl schon eingegeben. Willst du es ändern? (J/N): ")
        if frage.lower() != "j":
            return

    while True:
        gefuehl = input("Welches Gefühl hast du heute? ").lower()
        if gefuehl not in gefuehle:
            print("Unbekanntes Gefühl!")
            continue

        tage[tag] = [gefuehl, True]
        speichere_tage()
        print("Ihr Gefühl wurde gespeichert.")
        break

def gibTage():
    return tage

if __name__ == "__main__":
    main()
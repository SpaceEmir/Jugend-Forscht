import os

DATEI = "emotionen.json"
print("Çalışma dizini:", os.getcwd())
print("Script dizini:", os.path.dirname(os.path.abspath(__file__)))
print("Aranan dosya:", DATEI)
print("Dosya mevcut mu?", os.path.exists(DATEI))
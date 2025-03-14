auto = {"marca": "Fiat", "modello": "Panda", "cilindrata": 1200, "potenza": 60}
print(auto)
chiave = input("Inserisci la chiave da eliminare: ")
if chiave in auto:
    auto.pop(chiave)
    print(f"La chiave '{chiave}' è stata eliminata")
    print(auto)
else:
    print("La chiave non esiste")
    print(auto)
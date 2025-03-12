# parte 1
persona = {"nome": "Marco", "età": 17, "città": "Torino"}
print(persona["nome"])
print(persona["età"])
print(persona["città"])
# print(persona["professione"])

# parte 2
dati = {"nome": "Luca", "età": 30, "città": "Roma"}
print(dati.keys())
print(dati.values())
print(dati.items())

# parte 3
dizionario = {"a": 10, "b": 20, "c": 30}
chiave = "b"
if chiave in dizionario:
    print(f"La chiave '{chiave}' è presente nel dizionario con valore {dizionario.get(chiave)}")
else:
    print(f"Chiave non trovata, {dizionario.get(chiave)}")

# parte 4
dati = {"nome": "Giulia", "età": 22, "città": "Napoli", "indirizzo": "Via Garibaldi 111"}
dati.pop("indirizzo")
print(dati)
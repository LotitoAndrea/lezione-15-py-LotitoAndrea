libro = {"titolo": "Il signore degli anelli", "autore": "J.R.R. Tolkien", "anno di pubblicazione": 1954}
chiave = "editore"
print(libro)
if chiave in libro:
    print(f"La chiave '{chiave}' è presente nel dizionario con valore {libro.get(chiave)}")
else:
    print(f"Chiave non trovata, {libro.get(chiave)}")
    libro.update({chiave: "Mondadori"})
print(libro)
dizionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
media = sum(dizionario.values()) / len(dizionario)
print(f"La media dei valori del dizionario è {media}")
for i in dizionario:
    if dizionario[i] > media:
        print(i, dizionario[i])
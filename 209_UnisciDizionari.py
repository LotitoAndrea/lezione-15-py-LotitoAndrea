dizionario1 = {"nome": "Marco", "età": 19, "città": "Torino", "razza": "Umano"}
dizionario2 = {"nome": "Giovanni il distruttore di Galassie e automaton !!!", "razza": "Pastore Tedesco", "età": 3, "città": "Torino"}

for i in dizionario2:
    if type(dizionario2[i]) == int:
        dizionario1[i] = dizionario1.get(i, 0), dizionario2[i]
    if type(dizionario2[i]) == str:
        dizionario1[i] = dizionario1.get(i, "chiave non esistente"), dizionario2[i]
print(dizionario1)
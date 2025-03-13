listaDizionari = []
prezzoTotale = 0

dizionario1 = {"nome": "Latte", "prezzo": 1.20, "quantità": 2}
dizionario2 = {"nome": "Pane", "prezzo": 0.80, "quantità": 5}
dizionario3 = {"nome": "Uova", "prezzo": 0.25, "quantità": 12}
dizionario4 = {"nome": "Burro", "prezzo": 1.50, "quantità": 4}
listaDizionari.append([dizionario1, dizionario2, dizionario3, dizionario4])

for dizionario in listaDizionari:
    for prodotto in dizionario:
        prezzoTotale += prodotto["prezzo"] * prodotto["quantità"]
print(listaDizionari)
print(f"Il prezzo totale è di {prezzoTotale} euro")
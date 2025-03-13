persona = {"nome": "Marco", "età": 19, "città": "Torino"}
prodotto = {"prodotto": "Latte", "prezzo": 1.20, "quantità": 2}
animale = {"animale": "Cane", "razza": "Pastore Tedesco", "età": 3}

unione = {**persona, **prodotto, **animale}
print(unione)

# da finire
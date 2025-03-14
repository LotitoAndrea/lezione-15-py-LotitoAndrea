numero = int(input("Inserisci un numero: "))
dizionario = {}
for i in range(1, numero + 1):
    dizionario[i] = chr(96 + i) if i <= 26 else chr(64 + (i - 26))
dizionario_ordinato = dict(sorted(dizionario.items(), reverse=True))
print(dizionario_ordinato)
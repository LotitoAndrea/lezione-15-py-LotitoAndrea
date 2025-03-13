frase = input("Inserisci una frase: ")
parole = {}
for parola in range(0, len(frase)):
    if frase[parola] == " ":
        continue
    if frase[parola] in parole:
        parole[frase[parola]] += 1
    else:
        parole[frase[parola]] = 1
print(parole)
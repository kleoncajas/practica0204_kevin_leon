monedas = {"Euro" : "€", "Dollar" : "$", "Yen" : "¥"}
divisa = input("Escribe una divisa  ")
print(monedas.get(divisa, "La divisa no está en el diccionario"))
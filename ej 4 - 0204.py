dato = input("Introduce un dato sobre ti: ")
dato1 = input("- ")
usuario = {dato : dato1}
print(usuario)
seguir = input("¿Quieres introducir más datos sobre ti, si o no? ")
while seguir == "si":
    dato = input("Introduce un dato sobre ti: ")
    dato1 = input("- ")
    usuario[dato] = dato1
    print(usuario)
    seguir = input("¿Quieres introducir más datos sobre ti, si o no? ")
    if seguir == "no":
        exit()
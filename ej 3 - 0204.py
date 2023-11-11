productos = {"Pan" : 1.40, "Huevos" : 2.30, "Cebolla" : 0.85, "Aceite" : 4.35}
articulo = input("¿Qué articulo quieres?  ")
if articulo in productos:
    unidad = int(input("¿Cuántas unidades?  "))
    precio = unidad * productos[articulo]
    print(precio)
else:
    print("El producto no se encuentra disponible")
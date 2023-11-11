nombre = input("¿Cuál es tu nombre?  ")
edad = input("¿Cuál es tu edad?  ")
direccion = input("¿Cuál es tu dirección?  ")
telefono = input("¿Cuál es tu teléfono?  ")
usuario = {"nombre" : nombre, "edad" : edad, "direccion" : direccion, "telefono" : telefono}
print(usuario["nombre"], "tiene", usuario["edad"], "años, vive en", usuario["direccion"], "y su número de teléfono es", usuario["telefono"])
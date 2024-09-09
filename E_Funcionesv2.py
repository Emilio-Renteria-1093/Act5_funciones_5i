print("\n")
print("Funciones creda por el usuario")
print("------------------------------")


# lista
def mi_lista():
    print("Lista:\n")
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)
        
# llamar a funcione
mi_lista()
print("\n")
print("------------------------------")

# Tupla
def mi_tupla():
    print("Tupla:\n")
    comida=("tacos","burritos","gorditas")
    for yo in comida:
        print(yo)
        
mi_tupla()
print("\n")
print("------------------------------")

# Diccionario
def mi_diccionario():
        print("Diccionario:\n")
        carros={
        "marca": "gmc",
        "modelo": "sierra",
        "año": 2015
        }
        for key,value in carros.items():
            print(f"{key} : {value}")
        
        
mi_diccionario()
print("\n")
print("------------------------------")

# Arreglo
def mi_arreglo():
    print("Arreglo:\n")
    colores=("Azul","Negro","Rojo")
    for arcoiris in colores:
        print(arcoiris)
        
mi_arreglo()
print("\n")


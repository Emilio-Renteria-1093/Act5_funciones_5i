print("\n")
print("Manejo de funciones")
print("--------------------------------")

def hola_mundo():
    
    print("Hola aqui estoy")
    print("\n")
    print("--------------------------------")
    

def mensa(msg):
    print(msg)
    print("\n")
    

def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu nombre completo es {Nombre},{Apellido}")
    print("\n")
    print("--------------------------------")
    

def suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de {n1} + {n2} es :{s}"

# llamando a la funcion
hola_mundo()

mensa("Hola whatsapp") #Llama a la variable mensa con este parametro 

mensa("El profe me sorprendio enviando mensajes")#Vuelbe a llamar a mensa para mendarle otro parametro para mostrarlo
mensa("\n""--------------------------------")

EscribeNC("Eliseo","Nava")

print("Funciones que representan")
print(suma2numeros(7,3))
print(suma2numeros(15,45))

print("\n")
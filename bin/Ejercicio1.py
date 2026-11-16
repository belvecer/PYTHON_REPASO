from random import random


class Ejercicio1:

    nombre = "belen vera"
    nomMayus = nombre.title()
    numero = random.randint(1000, 9999)
    print(f"Socio{nomMayus}, Número de socio: {numero}")

    libros=["El Quijote", "1984", "Fahrenheit 451"]
    libros.append("Dune")
    libros.insert(1, "Drácula")
    eliminado = libros.pop(-1)
    print(len(libros))

    #Crea una función que reciba los días de retraso como parámetro posicional, 
    #y una tarifa fija por día que por defecto valga 0.50 (argumento por defecto).
    #Debe devolver el total a pagar.
    
    def calcular_multa(dias, tarita=0.50):
        total = dias * tarifa
        return total
    
    #El asterisco * antes de la variable 
    #le dice a Python: "guarda todos los textos que me pasen dentro de una tupla (como si fuera una lista)"    
    def registrar_prestamos(*libros): 
        print("Libros a prestar:")
        for libro in libros:
            print(f"{libros}")

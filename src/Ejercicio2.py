from random import random


class Ejercicio2:
    def generar_notas(cantidad):
        lista_notas=[]
        for i in range(cantidad): #range() para repetir cantidad veces
            nota= random.randint(0,10)
            lista_notas.append(nota)
        return lista_notas

nombres= ["Lola", "Dahlya", "Yinyo", "Nova"]
for nombre in nombres:
    print(f"Hola{nombres}, bienvenido al curso")


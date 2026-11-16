class Perro:
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza
        self.energia=100
    
    def ladrar(self):
        print(f"{self.nombre} esta ladrando: GUAU GAU!!")
    
perro1 = Perro("Firulais", "Pastor Aleman")
perro1.ladrar()

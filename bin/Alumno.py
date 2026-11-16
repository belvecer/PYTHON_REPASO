from Ejercicio2 import Alumno 
class Alumno:
    def __init__ (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self._matriculado=True

    def mostrar_info(self):
        print(f"Alumno: {self.nombre}, edad: {self.edad}")

print("Notas generadas:", generar_notas(5))
alumno1=Alumno("Lola", 20)
alumno1.mostrar_info()
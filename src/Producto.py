from Ejercicio3 import Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
        self._stock= generar_stock_aleatorio()

    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def stock(self):
        return self._stock
    
    @nombre.setter
    def nombre(self, value):
        self._nombre=value
    @precio.setter
    def pprecio(self, value):
        self._precio=value
    def __str__(self):
        return(f"Nombre: {self._nombre}, precio: {self._precio}, stock: {self._stock}")
p1 = Producto("Portatil", 800)
print(p1)
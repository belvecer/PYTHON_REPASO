class Libro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
        self._prestado=False

    @property
    def titulo(self):
        return self.titulo
    
    @property
    def autor(self):
        return self.autor
    
    @titulo.setter
    def titulo(self, value):
        self._titulo=value

    @autor.setter
    def autor(self, value):
        self._autor=value

    def __str__(self): #este seria el toString
        return f"Libro {self._titulo} escrito por: {self._autor}"

mi_libro: Libro("Cien años de soledad", "Gabriel García Marquez") # type: ignore
print(mi_libro)

        
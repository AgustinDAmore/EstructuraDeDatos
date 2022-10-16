class Pila:

    __slots__ = ['items', 'tamano']

    def __init__(self) -> None: 
        self.items = []
        self.tamano = 0
        
    def tamanio(self) -> int:
        return self.tamano

    def apilar(self, item) -> None:
        self.items.append(item)
        self.tamano += 1

    def desapilar(self) -> object:
        self.tamano -= 1
        return self.items.pop()

    def cima(self) -> object:
        return self.items[len(self.items)-1]
    
    def vacia(self) -> bool:
        return self.tamano == 0

    def mostrar(self) -> list:
        return self.items
    
    def vaciar(self):
        self.items = []
        self.tamano = 0

    def __repr__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return self.tamano
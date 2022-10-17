class Cola:

    __slots__ = ['items', 'tamano']

    def __init__(self):
        self.items = []
        self.tamano = 0

    def tamano(self):
        return self.tamano

    def EsVacia(self):
        return self.tamano == 0

    def encolar(self, item):
        self.items.append(item)
        self.tamano += 1

    def desencolar(self):
        self.tamano -= 1
        return self.items.pop(0)

    def frente(self):
        return self.items[0]
    
    def vaciar(self):
        self.items = []
        self.tamano = 0

    def __repr__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return self.tamano()


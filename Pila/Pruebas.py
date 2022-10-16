import Pila
#  probar la clase Pila
if __name__ == '__main__':
    p = Pila.Pila() # crear una pila vacía
    p.apilar(1) # apilar
    p.apilar(2)
    p.apilar(3)
    p.apilar(4)
    p.apilar(5)

    # ver tamaño de la pila
    print(len(p))
    print(p.tamanio())

    # mostrar la pila
    print(p) 
    print(p.mostrar())

    print(type(p))
    print(type(p.mostrar()))

    # recorrer la pila
    for item in p:
        print(item)

    # desapilar
    print(p.desapilar())
    p.vaciar()

    print(len(p))
class InstrumentoMusical:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Guitarra(InstrumentoMusical):
    def tocar(self):
        return f"{self.nombre} está tocando acordes de guitarra."

class Piano(InstrumentoMusical):
    def tocar(self):
        return f"{self.nombre} está tocando una melodía de piano."

class Flauta(InstrumentoMusical):
    def tocar(self):
        return f"{self.nombre} está tocando una melodía suave con la flauta."

class Bateria(InstrumentoMusical):
    def tocar(self):
        return f"{self.nombre} está tocando un ritmo de batería."

def gestionar_instrumentos(instrumentos):
    for instrumento in instrumentos:
        print(instrumento.tocar())

def mostrar_menu():
    print("\n--- Menú de Instrumentos Musicales ---")
    print("1. Ver y tocar Guitarra")
    print("2. Ver y tocar Piano")
    print("3. Ver y tocar Flauta")
    print("4. Ver y tocar Batería")
    print("5. Salir")

def main():
    # Crear instancias de instrumentos musicales
    guitarra = Guitarra("Guitarra Eléctrica")
    piano = Piano("Piano de Cola")
    flauta = Flauta("Flauta Traversera")
    bateria = Bateria("Batería Acústica")

    instrumentos = {
        1: guitarra,
        2: piano,
        3: flauta,
        4: bateria
    }

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 5:
                print("Saliendo del sistema.")
                break
            elif opcion in instrumentos:
                instrumento = instrumentos[opcion]
                print(instrumento.tocar())
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
# Definimos una clase base llamada 'Animal' que representa a un animal genérico.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una subclase llamada 'LoroRebelde' que hereda de 'Animal'.
class LoroRebelde(Animal):
    def __init__(self, nombre):
        # Llamamos al constructor de la clase base usando 'super()' para inicializar el nombre del animal.
        super().__init__(nombre)
        # Agregamos un atributo adicional 'es_rebelde' para el loro rebelde.
        self.es_rebelde = True

    def hablar(self, mensaje):
        # En el método 'hablar', verificamos si el loro es rebelde antes de permitir que hable.
        if self.es_rebelde:
            # Simulamos una interrupción por desbordamiento de lista al acceder a un índice fuera de los límites.
            lista = [1, 2, 3]
            try:
                valor = lista[4]
            except IndexError as e:
                print(f"Error: {e} (Desbordamiento de lista)")
            # Simulamos una interrupción por archivo no encontrado al intentar abrir un archivo inexistente.
            try:
                archivo = open("archivo_inexistente.txt", "r")
            except FileNotFoundError as e:
                print(f"Error: {e} (Archivo no encontrado)")
            # Lanzamos la excepción personalizada 'LoroRebeldeError'.
            raise LoroRebeldeError("¡El loro rebelde se ha escapado!")

# Definimos una excepción personalizada llamada 'LoroRebeldeError'.
class LoroRebeldeError(Exception):
    pass

# Creamos una función llamada 'gestionar_loro_rebelde' para manejar al loro rebelde.
def gestionar_loro_rebelde():
    # Creamos una instancia de 'LoroRebelde' llamada 'loro'.
    loro = LoroRebelde("Lorenzo")
    
    try:
        # Intentamos que el loro hable.
        loro.hablar("¡Hola, soy Lorenzo!")
    except LoroRebeldeError as e:
        # Capturamos la excepción 'LoroRebeldeError' si se lanza.
        print(f"Error: {e}")
        print("Vamos a tratar de calmar al loro rebelde...")
        # Llamamos a la función 'calmado_loro_rebelde()' para intentar calmar al loro.
        calmado = calmado_loro_rebelde()
        if calmado:
            print("¡El loro rebelde ha sido calmado y ha vuelto a su jaula!")
        else:
            print("¡El loro rebelde sigue siendo rebelde y causa caos en el zoológico!")

# Creamos una función llamada 'calmado_loro_rebelde' que simula intentar calmar al loro rebelde.
def calmado_loro_rebelde():
    # Simulamos una acción para calmar al loro rebelde. En este caso, la acción no tiene éxito.
    return False  # El loro sigue siendo rebelde

# Verificamos si este archivo se ejecuta como el programa principal.
if __name__ == "__main__":
    print("Bienvenido al Zoológico de Animales Exóticos")
    print("Gestionando el problema del loro rebelde...")
    # Llamamos a la función 'gestionar_loro_rebelde()' para comenzar a manejar al loro rebelde.
    gestionar_loro_rebelde()
    print("Fin del programa")


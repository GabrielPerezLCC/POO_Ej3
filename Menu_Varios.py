class Menu:
    @classmethod
    def menuOpciones(cls):
        while True:
            print("Menú de opciones:")
            print("1- Mostrar día y hora de menor y mayor valor por variable.")
            print("2- Indicar temperatura promedio mensual por cada hora.")
            print("3- Listar valores de las tres variables para un día dado.")
            print("4- Salir")
            opcion = input("Elija la opción deseada: ")
            if opcion in ["1", "2", "3", "4"]:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

def Saludar_Usuario():
    Nombre_Usuario = input("Escribe tu nombre: ")

    Mensaje = f" ¡Hello {Nombre_Usuario}! welcome to our personalized program, ¡enjoy the process! "
    print(Mensaje)


Saludar_Usuario()

def contador_de_numeros():
    try:

        numero_ingresado = int(input("Ingrese un número entero: "))


        if numero_ingresado <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return


        for i in range(1, numero_ingresado + 1):
            print(i)

    except ValueError:
        print("Por favor, ingrese un número entero válido.")


contador_de_numeros()
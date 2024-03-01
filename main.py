
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


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def main():
    print("Calculadora Básica")
    print("Operaciones disponibles: suma, resta, multiplicación, división")

    operacion = input("Ingrese la operación deseada: ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "suma":
        resultado = suma(num1, num2)
    elif operacion == "resta":
        resultado = resta(num1, num2)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(num1, num2)
    elif operacion == "division":
        resultado = division(num1, num2)
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()



#%%

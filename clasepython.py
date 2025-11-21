print("Bienvenido a la calculadora")

operaciones = ["+", "-", "*", "/"]

while True:
    n1 = input("Ingresa el número 1 (o escribe 'salir' para terminar): ")
    if n1.lower() == "salir":
        print("Programa terminado.")
        break

    # Verificar que n1 sea un número válido
    try:
        n1 = float(n1)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    oper = input("Ingresa la operación (+, -, *, /) o escribe 'salir' para terminar: ")
    if oper.lower() == "salir":
        print("Programa terminado.")
        break

    # Validar operación
    if oper not in operaciones:
        print("Operación no válida. Intenta con +, -, * o /.")
        continue

    n2 = input("Ingresa el número 2 (o escribe 'salir' para terminar): ")
    if n2.lower() == "salir":
        print("Programa terminado.")
        break

    # Verificar que n2 sea un número válido
    try:
        n2 = float(n2)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    # Realizar la operación
    if oper == '+':
        resultado = n1 + n2
    elif oper == '-':
        resultado = n1 - n2
    elif oper == '*':
        resultado = n1 * n2
    elif oper == '/':
        # Validar división entre cero
        if n2 == 0:
            print("Error: no se puede dividir entre cero.")
            continue
        resultado = n1 / n2

    print(f"El resultado de {n1} {oper} {n2} es: {resultado}")

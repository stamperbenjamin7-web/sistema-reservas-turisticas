# Defina una función que nos permita determinar si una variable
# es un palindromo
def palindromo(texto):
    texto_sin_espacios = remote_space(texto.lower())
    texto_invertido = reverse(texto_sin_espacios)

    if (texto_invertido == texto_sin_espacios):
        return "es un palindromo"
    else:
        return "no es un palindromo"


def reverse(texto):
    texto_invertido = ""
    for chart in texto:
        texto_invertido = chart + texto_invertido
    return texto_invertido


def remote_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != "":
            nuevo_texto += char
    return nuevo_texto


def palindromoAvanzado(texto):
    # Convertimos todo el texto a minúsculas para que sea insensible a mayúsculas
    texto = texto.lower()

    # Eliminamos espacios para que no interfieran en la verificación
    texto = texto.replace(" ", "")

    # Verificamos si el texto es igual a su reverso
    if texto == texto[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"


print("Abba", palindromo("Abba"))
print("Reconocer", palindromo("reconocer"))
print("Hola mundo", palindromo("Hola mundo"))

import sys

def cifrado_cesar(texto, corrimiento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            if char.islower():
                nuevo_char = chr((ord(char) - ord('a') + corrimiento) % 26 + ord('a'))
            else:
                nuevo_char = chr((ord(char) - ord('A') + corrimiento) % 26 + ord('A'))
            texto_cifrado += nuevo_char
        else:
            texto_cifrado += char
    return texto_cifrado

# Obtener los argumentos de la línea de comandos
if len(sys.argv) != 3:
    sys.exit(1)

texto = sys.argv[1]
corrimiento = int(sys.argv[2])

# Aplicar el cifrado César e imprimir el texto cifrado
texto_cifrado = cifrado_cesar(texto, corrimiento)
print(texto_cifrado)



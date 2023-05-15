def invertir_cadena(cadena):
    # Convertir la cadena en una lista de caracteres
    caracteres = list(cadena)

    # Invertir la lista de caracteres
    caracteres.reverse()

    # Unir los caracteres invertidos para formar la cadena invertida
    cadena_invertida = ''.join(caracteres)

    return cadena_invertida

# Ejemplo de uso
cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)

print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)

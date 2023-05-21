# Diccionario user_profile sin nada asignado
user_profile = {"nombre": None, "edad": None, "profesion": None, "ciudad": None}

# Diccionario user_input con valores asignados
user_input = {
    "nombre": "Juan",
    "edad": 25,
    "profesion": "Ingeniero",
    "ciudad": "Madrid",
}

# haz esto
user_profile |= user_input
print(user_profile)
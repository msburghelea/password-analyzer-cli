import json
import math
import hibp
from collections import Counter

def obtener_datos():
    with open("passwords.txt", "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)
contraseñas_comunes = obtener_datos()
def contrasena_comun(password):
    return password in contraseñas_comunes

def analizar(password, check=False):
    has_upper, has_lower, has_digit, has_special = evaluar_complejidad(password)
    resultado = {
        "longitud": evaluar_longitud(password),
        "complejidad": {
            "tiene_mayusculas": has_upper,
            "tiene_minusculas": has_lower,
            "tiene_digitos": has_digit,
            "tiene_especiales": has_special
        },
        "entropia_shannon": entropia_shannon(password),
        "entropia_bits": entropia_bits(password),
        "es_comun": contrasena_comun(password) if check else "No verificado",
        "hibp": hibp.comprobar_hibp(password) if check else "No verificado"
    }
    return resultado

def imprimir_resultados(resultado):
    print(json.dumps(resultado, indent=4, ensure_ascii=False))

def evaluar_longitud(password):
    if len(password) < 8:
        return "Débil"
    elif len(password) < 12:
        return "Media"
    else:
        return "Fuerte"
    
def evaluar_complejidad(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper, has_lower, has_digit, has_special

def entropia_shannon(password):
    
    conteos = Counter(password)
    entropia = 0

    for char, count in conteos.items():
        probabilidad = count / len(password)
        entropia += -probabilidad * math.log2(probabilidad)

    return entropia


def entropia_bits(password):
    has_upper, has_lower, has_digit, has_special = evaluar_complejidad(password)

    pool = 0

    if has_upper:
        pool += 26

    if has_lower:
        pool += 26

    if has_digit:
        pool += 10

    if has_special:
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)



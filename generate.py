import secrets
import string

def generar_contrasena(longitud):
    contrasena = [secrets.choice(string.ascii_uppercase),
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.digits),
    secrets.choice(string.punctuation)]
   
    for i in range(longitud-4):
        contrasena.append(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
)
    secrets.SystemRandom().shuffle(contrasena)
    resultado = "".join(contrasena)
    print(resultado)
    return resultado


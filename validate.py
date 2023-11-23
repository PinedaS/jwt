import jwt

token = input("Ingresa el token: ")
secret_key = "mysecret"

try:
    payload = jwt.decode(token, secret_key, algorithms=["HS256"])
except jwt.exceptions.ExpiredSignatureError:
    print("El token ha expirado.")
except jwt.exceptions.InvalidSignatureError:
    print("La firma no es válida.")
except jwt.exceptions.DecodeError:
    print("El token no es válido.")
else:
    print("Token válido!")

import jwt
from datetime import datetime

iat = datetime.now()
unix_time_iat = iat.timestamp()

expire_at = iat.replace(year=iat.year + 1)
unix_time_expire_at = expire_at.timestamp()

payload = {
    "username": "Sebastián Pineda",
    "email": "spineda0424@gmail.com",
    "iat": unix_time_iat,
    "exp": unix_time_expire_at
}

secret = "mysecret"

encoded_token = jwt.encode(payload, secret, algorithm="HS256")
print(encoded_token)

from hashlib import sha256


def encrypt_token(token: str, timestamp: str):
    return sha256((token+timestamp).encode("utf-8")).hexdigest()

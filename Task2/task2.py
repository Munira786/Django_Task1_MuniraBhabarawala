import secrets
import string
import base64
from typing import Tuple
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


def generate_otp() -> str:
    """Generate a 6-character OTP with 2 uppercase, 2 special chars, 2 digits"""
    rng = secrets.SystemRandom()
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*()-_=+[]{}:,.?"

    parts = [
        rng.choice(uppercase),
        rng.choice(uppercase),
        rng.choice(specials),
        rng.choice(specials),
        rng.choice(digits),
        rng.choice(digits),
    ]
    rng.shuffle(parts)
    return "".join(parts)


def generate_rsa_keypair(key_size: int = 2048) -> Tuple[bytes, bytes]:
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=key_size, backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return private_pem, public_pem


def encrypt_with_public_key(plaintext: str, public_pem: bytes) -> bytes:
    public_key = serialization.load_pem_public_key(public_pem, backend=default_backend())
    ciphertext = public_key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    return ciphertext


def decrypt_with_private_key(ciphertext: bytes, private_pem: bytes) -> str:
    private_key = serialization.load_pem_private_key(private_pem, password=None, backend=default_backend())
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    return plaintext.decode("utf-8")


def demo():
    otp = generate_otp()
    print("Generated OTP:", otp)

    private_pem, public_pem = generate_rsa_keypair()
    ciphertext = encrypt_with_public_key(otp, public_pem)
    b64_cipher = base64.b64encode(ciphertext).decode()
    print("Encrypted OTP (base64):", b64_cipher)

    decrypted = decrypt_with_private_key(base64.b64decode(b64_cipher), private_pem)
    print("Decrypted OTP:", decrypted)


if __name__ == "__main__":
    demo()

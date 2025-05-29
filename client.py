# client.py
"""
Cliente SPEKE (Alice).
Se conecta con un servidor, intercambia claves públicas derivadas de una contraseña compartida
y calcula una clave secreta sin revelar la contraseña.
"""

import socket
import secrets
from speke_common import p, derive_generator

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432
KEY_SIZE = 256  # Tamaño en bytes para representar claves grandes


def main():
    # Ingreso de la contraseña compartida
    password = input("[Cliente] Ingrese contraseña compartida: ").strip()
    g = derive_generator(password)

    # Generación de secreto privado a y clave pública A
    a = secrets.randbelow(p)
    A = pow(g, a, p)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[Cliente] Conectado con el servidor")

        # Enviar clave pública A al servidor (Bob)
        s.sendall(A.to_bytes(KEY_SIZE, byteorder='big'))

        # Recibir clave pública B desde el servidor
        B_bytes = s.recv(KEY_SIZE)
        B = int.from_bytes(B_bytes, byteorder='big')
        print(f"[Cliente] Recibido B: {B}")

        # Derivar clave secreta compartida
        K_alice = pow(B, a, p)
        print(f"[Cliente] Clave derivada: {K_alice}")


if __name__ == "__main__":
    main()

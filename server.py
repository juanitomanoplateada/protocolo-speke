# server.py
"""
Servidor SPEKE (Bob).
Recibe conexión de un cliente, intercambia claves públicas derivadas de una contraseña compartida
y calcula una clave secreta sin revelar la contraseña.
"""

import socket
import secrets
from speke_common import p, derive_generator

# Dirección y puerto para la conexión
HOST = '127.0.0.1'
PORT = 65432
KEY_SIZE = 256  # Tamaño en bytes para representar claves grandes


def main():
    # Ingreso de la contraseña compartida
    password = input("[Servidor] Ingrese contraseña compartida: ").strip()
    g = derive_generator(password)

    # Generación de secreto privado b y clave pública B
    b = secrets.randbelow(p)
    B = pow(g, b, p)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("[Servidor] Esperando conexión...")

        conn, addr = s.accept()
        with conn:
            print(f"[Servidor] Conectado con {addr}")

            # Recibir clave pública A del cliente (Alice)
            A_bytes = conn.recv(KEY_SIZE)
            A = int.from_bytes(A_bytes, byteorder='big')
            print(f"[Servidor] Recibido A: {A}")

            # Enviar clave pública B al cliente
            conn.sendall(B.to_bytes(KEY_SIZE, byteorder='big'))

            # Derivar clave secreta compartida
            K_bob = pow(A, b, p)
            print(f"[Servidor] Clave derivada: {K_bob}")


if __name__ == "__main__":
    main()

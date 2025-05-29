# speke_common.py
"""
Módulo común para la implementación de SPEKE.
Contiene el número primo p y la función para derivar el generador g
a partir de una contraseña compartida.
"""

import hashlib

# Número primo grande seguro (puede ser sustituido por uno más robusto si se desea)
p = 0xE95E4A5F737059DC60DFC7AD95B3D8139515620F


def derive_generator(password: str) -> int:
    """
    Deriva un generador g a partir de una contraseña usando SHA-256.

    Parámetros:
        password (str): Contraseña compartida.

    Retorna:
        int: Generador derivado (g = H(password)^2 mod p).
    """
    h = hashlib.sha256(password.encode()).hexdigest()
    g = pow(int(h, 16), 2, p)
    return g

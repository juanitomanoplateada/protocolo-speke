# test_speke.py
"""
Test automatizado del protocolo SPEKE.
Verifica tanto el mejor caso (claves coinciden) como el peor caso (claves distintas).
"""

import secrets
from speke_common import p, derive_generator

def speke_simulation(password_alice: str, password_bob: str):
    """
    Simula el intercambio SPEKE entre Alice y Bob con contraseñas potencialmente distintas.

    Parámetros:
        password_alice (str): Contraseña usada por Alice.
        password_bob (str): Contraseña usada por Bob.

    Retorna:
        (clave de Alice, clave de Bob, bool indicando si coinciden)
    """
    # Cada parte deriva su propio generador g
    g_alice = derive_generator(password_alice)
    g_bob = derive_generator(password_bob)

    # Claves privadas
    a = secrets.randbelow(p)
    b = secrets.randbelow(p)

    # Claves públicas
    A = pow(g_alice, a, p)
    B = pow(g_bob, b, p)

    # Derivación de clave común
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)

    return K_alice, K_bob, K_alice == K_bob

def test_best_case():
    print("\n== ✅ CASO EXITOSO: Contraseña igual ==")
    password = "claveSuperSegura2025"
    K_alice, K_bob, success = speke_simulation(password, password)
    print(f"Clave de Alice: {K_alice}")
    print(f"Clave de Bob:   {K_bob}")
    print("[Resultado]:", "✔ Claves coinciden" if success else "❌ Claves distintas")

def test_worst_case():
    print("\n== ❌ CASO FALLIDO: Contraseñas diferentes ==")
    password_alice = "claveCorrecta"
    password_bob = "claveIncorrecta"
    K_alice, K_bob, success = speke_simulation(password_alice, password_bob)
    print(f"Clave de Alice: {K_alice}")
    print(f"Clave de Bob:   {K_bob}")
    print("[Resultado]:", "✔ Claves coinciden" if success else "❌ Claves distintas (esperado)")

def test_edge_case_empty_password():
    print("\n== ⚠️ CASO BORDE: Contraseña vacía ==")
    K_alice, K_bob, success = speke_simulation("", "")
    print(f"Clave de Alice: {K_alice}")
    print(f"Clave de Bob:   {K_bob}")
    print("[Resultado]:", "✔ Claves coinciden" if success else "❌ Claves distintas")

if __name__ == "__main__":
    test_best_case()
    test_worst_case()
    test_edge_case_empty_password()

# 🔐 SPEKE 3.1 – Simple Password Exponential Key Exchange

Una implementación funcional en Python del protocolo **SPEKE**, diseñado para realizar el intercambio seguro de claves basado en una contraseña compartida, sin exponer dicha contraseña ni permitir ataques offline.

## 📜 Descripción General

SPEKE es un protocolo de tipo PAKE (Password Authenticated Key Exchange) que permite a dos partes (Alice y Bob) acordar una clave secreta común únicamente con una contraseña mutua. Se basa en el protocolo de Diffie-Hellman, pero con autenticación derivando el generador del grupo a partir de la contraseña mediante hashing criptográfico.

### Ventajas:
- No se transmite la contraseña.
- Resistencia a ataques de diccionario offline.
- Protección contra ataques de repetición y man-in-the-middle.
- No requiere base de datos de contraseñas.
- Autenticación mutua implícita.

## 📁 Estructura del Proyecto

```
.
├── speke_common.py     # Lógica común: primo seguro y función de derivación de generador
├── server.py           # Rol del servidor (Bob)
├── client.py           # Rol del cliente (Alice)
├── test_speke.py       # Casos de prueba automatizados
└── README.md           # Este archivo
```

## ⚙️ Requisitos

- Python 3.8 o superior

## 🚀 Ejecución

### 1. Inicia el servidor

```bash
python3 server.py
```

Ingresa la contraseña compartida cuando se solicite.

### 2. Inicia el cliente en otra terminal

```bash
python3 client.py
```

Ingresa **la misma** contraseña que en el servidor.

Si las contraseñas coinciden, ambos derivan la misma clave secreta (K). De lo contrario, obtendrán claves diferentes.

## 🧪 Pruebas

Para validar el comportamiento del protocolo ante diferentes escenarios:

```bash
python3 test_speke.py
```

Casos probados:
- ✅ Contraseñas iguales (éxito esperado)
- ❌ Contraseñas distintas (fallo esperado)
- ⚠️ Contraseña vacía (comportamiento lógico pero inseguro)

## 🔐 Seguridad

- **Diccionario offline**: No es posible probar contraseñas sin interacción activa.
- **MitM (Hombre en el medio)**: La contraseña compartida es necesaria para obtener un generador válido, lo que previene la intrusión.
- **Repetición**: Cada ejecución es única por el uso de claves efímeras.
- **Subgrupos pequeños**: Puede mejorarse añadiendo validación de rango para `A` y `B`.

## 💡 Detalles Técnicos

- **Generador derivado**: `g = H(password)^2 mod p` (SHA-256)
- **Clave secreta común**: `K = g^{ab} mod p`, obtenida de forma independiente por cada parte.
- **No se transmite ni la contraseña ni su hash directo.**

## 📌 Notas de Implementación

- El número primo `p` puede ser sustituido por uno más robusto si se desea aumentar la seguridad.
- Se recomienda añadir una fase explícita de *key confirmation* (por ejemplo, usando HMAC sobre `K`).
- Evitar contraseñas vacías o triviales en producción.

## 📚 Créditos

Desarrollado como simulación educativa del protocolo SPEKE (PAKE). Basado en estándares criptográficos y buenas prácticas de seguridad informática.

---

🛡️ Protocolo robusto. Contraseñas simples. Sesiones seguras.

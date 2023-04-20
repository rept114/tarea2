import hashlib

# Pedir al usuario un dato de entrada
dato = input("Ingresa un dato: ")

# Aplicar la función hash sha1
h = hashlib.sha1(dato.encode())
print("sha1:", h.hexdigest())

# Aplicar la función hash sha224
h = hashlib.sha224(dato.encode())
print("sha224:", h.hexdigest())

# Aplicar la función hash sha256
h = hashlib.sha256(dato.encode())
print("sha256:", h.hexdigest())

# Aplicar la función hash sha384
h = hashlib.sha384(dato.encode())
print("sha384:", h.hexdigest())

# Aplicar la función hash sha512
h = hashlib.sha512(dato.encode())
print("sha512:", h.hexdigest())

# Aplicar la función hash blake2b
h = hashlib.blake2b(dato.encode())
print("blake2b:", h.hexdigest())

# Aplicar la función hash blake2s
h = hashlib.blake2s(dato.encode())
print("blake2s:", h.hexdigest())

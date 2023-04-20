import hashlib

# Pedir al usuario un dato de entrada
dato = input("Ingresa un dato: ")
dato2 = input("Ingresa un dato: ")
dato3 = input("Ingresa un dato: ")
dato4 = input("Ingresa un dato: ")
dato5 = input("Ingresa un dato: ")
dato6 = input("Ingresa un dato: ")
dato7 = input("Ingresa un dato: ")

# Aplicar la función hash sha1
h = hashlib.sha1(dato.encode())
print("sha1:", h.hexdigest())

# Aplicar la función hash sha224
h = hashlib.sha224(dato2.encode())
print("sha224:", h.hexdigest())

# Aplicar la función hash sha256
h = hashlib.sha256(dato3.encode())
print("sha256:", h.hexdigest())

# Aplicar la función hash sha384
h = hashlib.sha384(dato4.encode())
print("sha384:", h.hexdigest())

# Aplicar la función hash sha512
h = hashlib.sha512(dato5.encode())
print("sha512:", h.hexdigest())

# Aplicar la función hash blake2b
h = hashlib.blake2b(dato6.encode())
print("blake2b:", h.hexdigest())

# Aplicar la función hash blake2s
h = hashlib.blake2s(dato7.encode())
print("blake2s:", h.hexdigest())

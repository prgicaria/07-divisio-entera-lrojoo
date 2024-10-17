# Demanar el dividend i el divisor a l'usuari
dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))

# Calcular el quocient i el residu
quocient = dividend // divisor
residu = dividend % divisor

# Mostrar els resultats segons l'exemple
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")


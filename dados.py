import random

def lanzar_dados(num_dados):
    if num_dados not in [1, 2, 3]:
        raise ValueError("El número de dados debe ser 1, 2 o 3.")
    
    suma = 0
    for _ in range(num_dados):
        dado = random.randint(1, 6)
        suma += dado
        print(f"Dado: {dado}")
    
    print(f"Suma total: {suma}")
    return suma

# Ejemplo de uso
num_dados = int(input("¿Cuántos dados quieres lanzar (1, 2 o 3)? "))
lanzar_dados(num_dados)
import math

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejemplo de uso
radio = 7
perimetro = calcular_perimetro_circulo(radio)
print(f"El perímetro del círculo con radio {radio} es {perimetro}")
def calcular_volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

# Ejemplo de uso
volumen = calcular_volumen_esfera(radio)
print(f"El volumen de la esfera con radio {radio} es {volumen}")
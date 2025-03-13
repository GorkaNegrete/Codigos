import numpy as np
import scipy as sp
import sympy as sym
import math
# Definir el vector de aceleraciones en mm
atotal_mm = np.array([4.6437, 2.4073, 4.7184]) 
# Convertir aceleraciones a metros
atotal_m = atotal_mm / 1000
# Definir la masa en kg
mass = .368
# Definir la gravedad en m/s^2
gravity = 9.81
# Definir el vector z
z_vector = np.array([0, 0, 1])
# Calcular la fuerza del gripper en vector
F_gripper_v = (mass * atotal_m)+(mass*gravity*z_vector)
# Calcular la magnitud de la fuerza del gripper
F_gripper_m = np.linalg.norm(F_gripper_v)
# Imprimir los resultados
print(F_gripper_v)
print(F_gripper_m)
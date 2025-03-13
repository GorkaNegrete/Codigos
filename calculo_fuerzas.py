import numpy as np
import scipy as sp
import sympy as sym
import math
atotal_mm = np.array([4.6437, 2.4073, 4.7184])
atotal_m = atotal_mm / 1000
mass = .368
gravity = 9.81
z_vector = np.array([0, 0, 1])
F_gripper_v = (mass * atotal_m)+(mass*gravity*z_vector)
F_gripper_m = np.linalg.norm(F_gripper_v)
print(F_gripper_v)
print(F_gripper_m)
import numpy as np
# Ax=b
class EquationSystem:
    def __init__(self, coefficients, constants, variables, isLinear=True):
        self.A = coefficients # matrix A
        self.b = constants # matrix B
        self.variables=variables
        self.is_linear=isLinear # boolean
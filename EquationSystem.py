# Ax=b
class EquationSystem:
    def __init__(self, coefficients, constants, isLinear):
        if (not self.validate(coefficients,constants)):
            return None
        self.coefficients = coefficients # matrix A
        self.constants = constants # matrix B
        self.is_linear=isLinear # boolean
    
    def validate(coefficients,constants):
        for row in coefficients:
            for elem in row:
                if (not elem.isdigit()) and (not elem.isalpha()): 
                    return False
                
        for elem in constants:
            if (not elem.isdigit()) and (not elem.isalpha()): 
                return False

        return True
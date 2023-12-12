class EquationSystem:
    def __init__(self, coefficients, isLinear):
        if (not self.validate(coefficients)):
            return None
        self.coefficients = coefficients # matrix
        self.is_linear=isLinear # boolean
    
    def validate(coefficients):
        for row in coefficients:
            for elem in row:
                if (not elem.isdigit()) and (not elem.isalpha()): 
                    return False
        return True
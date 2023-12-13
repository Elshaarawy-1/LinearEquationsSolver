import Solver
import numpy as np

class JacobiSolver(Solver):
    
    
    def __init__(self, A, b, itr=50, tolerance=1e-10, initGuess=None):
        self.A = A
        self.b = b
        self.itr = itr
        self.tolerance = tolerance
        self.initGuess = initGuess
        
        pass
    
    
    
    def solve(self):
        
        x = self.initGuess.copy()
        D = np.diag(self.A) #extract diagonal elements of A
        R = self.A - D #extract non-diagonal elements of A
        #check if the diagonal elements are zero
        # if(np.any(D==0)):
            #handel the case using diagnonally dominant matrix
           
        for i in range(self.itr):
            print('Iteration: {i+1}: ')
            x_old = x.copy()
            x = (self.b-np.dot(R,x_old))/D
            for j in range(len(x)):
                abs_error = abs(x[j]-x_old[j])/abs(x[j])
                print(f'x{j+1} = {x[j]},      absolute error = {abs_error}')
            #check if all the absolute errors are less than tolerance
            if(np.all(abs_error) < self.tolerance):
                break
          
        return x  
        pass  
        
import numpy as np
import mpmath

def diagonally_dominant(array, x_order,parsed_bef):
        abs_matrix = np.absolute(array)
        diagonal = np.diag(abs_matrix)
        greater = False
        gr_eq = True
        for i in range(abs_matrix.shape[0]):
            if diagonal[i] > np.sum(abs_matrix,axis=1)[i] - diagonal[i]:
                greater = True
            elif diagonal[i] == np.sum(abs_matrix,axis=1)[i] - diagonal[i]:
                continue
            else:
                gr_eq = False
                break
        
        if greater and gr_eq:
            return array,True
        else:
            return array ,False
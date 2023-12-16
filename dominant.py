import numpy as np


def diagonally_dominant(array, parsed_bef):
        abs_matrix = np.absolute(array.tolist())
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
            return array, True
        elif not parsed_bef:
            return convert_matrix(array)
        else:
            return array, False

def convert_matrix(array):
        abs_matrix = np.absolute(array)
        max_indices = np.argmax(abs_matrix, axis=1)
        #Check if the matrix can be converted into diagonal diagonally dominant one
        if len(np.unique(max_indices)) != len(max_indices):
            return array, False
        
        for i in range(array.shape[0]):
            max_ind = np.argmax(abs_matrix[i])
            if i != max_ind:
                array[:,[i,max_ind]] = array[:, [max_ind,i]]
                abs_matrix[:, [i,max_ind]] = abs_matrix[:, [max_ind,i]]

        return diagonally_dominant(array,True)
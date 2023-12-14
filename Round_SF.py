import numpy as np


def round_to_sf(number, sf):
        if number == 0:
            return 0
        order_of_magnitude = 10 ** (sf -
                                    int(np.floor(np.log10(abs(number)))) - 1)
        rounded_number = round(
            number * order_of_magnitude) / order_of_magnitude
        return rounded_number

def round_matrix_to_sf(matrix, sf):
      
        rounded_matrix = np.vectorize(
            lambda x: round_to_sf(x, sf))(matrix)
        return rounded_matrix
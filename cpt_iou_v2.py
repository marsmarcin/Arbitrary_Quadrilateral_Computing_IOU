
import numpy as np

def vector_product(coord):
    coord = np.array(coord).reshape((4,2))
    temp_det = 0
    for idx in range(3):
        temp = np.array([coord[idx],coord[idx+1]])
        temp_det +=np.linalg.det(temp)
    temp_det += np.linalg.det(np.array([coord[-1],coord[0]]))
    return temp_det*0.5
coord = [908,215,934,312,752,355,728,252]

vector_result = vector_product(coord)
coord1=[923,308,758,342,741,262,907,228]


print(vector_result)
vector_result1 = vector_product(coord1)
print(vector_result1)
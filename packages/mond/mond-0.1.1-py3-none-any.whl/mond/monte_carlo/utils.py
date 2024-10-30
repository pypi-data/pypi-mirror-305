from typing import List 
import math
import numpy as np 
from random import uniform

def random_rotate(mol_xyz:List[List[float]])->List[List[float]]:
    """
    Random rotation of a list of xyz coordinates
    """
    rot_matrix = generate_random_rotation_matrix()
    rotated_mol = rotate(rot_mat, mol_xyz)
    return rotated_mol

def rotate(rot_mat:List[List[float]], mol_xyz:List[List[float]])->List[List[float]]: 
    """
    Rotates a molecule given a specific rotation matrix
    """
    raise NotImplementedError

def generate_random_rotation_matrix()-> List[List[float]]: 
    
    alpha = uniform(0, 360)
    beta = uniform(0, 360)
    gamma = uniform(0, 360)

    r_x = [[1 , 0 , 0], 
           [0, cos(alpha), -sin(alpha)], 
           [0, sin(alpha), cos(alpha)]]
           
    r_y = [[cos(beta), 0, sin(beta)],
            [0, 1, 0], 
            [-sin(beta), 0, cos(beta)]]

    r_z = [[cos(gamma), -sin(gamma), 0], 
           [sin(gamma), cos(gamma), 0],
           [0, 0, 1]]

    random_matrix = list(np.dot(r_x, r_y, r_z))
    return random_matrix

def generate_random_translation_matrix()->None: 
    raise NotImplementedError
    
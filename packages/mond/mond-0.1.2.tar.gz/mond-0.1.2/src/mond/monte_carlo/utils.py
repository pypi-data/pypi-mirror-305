from typing import List 
from math import cos, sin
import numpy as np 
from random import uniform

def random_rotate(mol_coords:List[List[float]])->List[List[float]]:
    """
    Random rotation of a list of xyz coordinates
    """
    rot_mat = generate_random_rotation_matrix()
    rotated_mol = rotate(rot_mat, mol_coords)
    return rotated_mol

def rotate(rot_mat:List[List[float]], mol_coords:List[List[float]])->List[List[float]]: 
    """
    Rotates a molecule given a specific rotation matrix
    """
    rotated_mol = np.dot(rot_mat, mol_coords).tolist()
    return rotated_mol

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

    random_matrix = np.dot(r_y, r_z)
    random_matrix = np.dot(r_x, random_matrix)
    return random_matrix

def generate_random_translation_matrix()->None: 
    raise NotImplementedError
    
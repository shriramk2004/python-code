## numpy library ###
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array = np.arange(9)
mean_value = np.mean(array) 
max_value = np.max(array) 
min_value = np.min(array)  
std_dev = np.std(array)   

product_of_matrix = np.dot(array_2d, array_2d) 
transpose_of_matrix = np.transpose(array_2d)

random_array = np.random.rand(3, 3)
rand_int = np.random.randint(1, 10) 
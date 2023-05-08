# General Python
m = [ [ [243, 2, 34], (244, 59, 56) ], 77, 18 ]
print(len(m))
print(m[0][0][1])

my_tuple = ('Truck', [28, True])
print(my_tuple[0][-1])

my_str = '()A()A()'
# my_str = my_str.plit('A') what you want to spliy by is A
# wb = write in binary in pickel serialization

class Kevin:
    """Class Kevin"""
    def __init__(self, name):
        self.name = name
        self.otter_id = 374587
    def __str__(self):
        return "Kevin is awesome"
    def __eq__(self, other):
        return self.otter_id == other.otter_id

import numpy as np
x = [1,4]

x_p2 = np.array(x)
print(np.repeat(x_p2, 5))
print(x_p2 * 3)

x_np = np.array(np.arange(1500))

# convert to grayscake when detecing faces
#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version)
print('\n')

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(10, size = (2, 3, 5))


#4. Print a.

print(f"array of a is \n {a}")

print('\n')

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3), dtype=int)

#6. Print b.

print(f"array of b is \n {b}")
print('\n')

#7. Do a and b have the same size? How do you prove that in Python code?

a.size == b.size
print(f"Size of a is {a.size}")
print(f"Size of b is {b.size}")
print('\n')

#8. Are you able to add a and b? Why or why not?

# No. They have different shapes.
print(f"Shape of a is {a.shape}")
print(f"Shape of b is {b.shape}")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)
print(f"Shape of c is {c.shape}")
print("\n")

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

# They have both the same shape. 

d = a + c


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(f"array of d (sum of b and c) is \n {d}")
print('\n')
print(f"array of a is \n {a}")
print("\n")

# En términos de valores vemos que los valores del array d tienen una unidad más.

#12. Multiply a and c. Assign the result to e.

e = a*c
print(f"array of e (product of a and c) is \n {e}")

#13. Does e equal to a? Why or why not?

# Both arrays e and a are equal.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = a.max()
d_min= a.min()
d_mean = a.mean()

print("\n")
print(f"max value of array d is {d_max}")
print("\n")
print(f"max value of array d is {d_min}")
print("\n")
print(f"max value of array d is {d_mean}")


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5), int)
print(f)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for el in range(2):
        for els in range(3):
                for ells in range(5):
                        if d[el][els][ells] > d_min and d[el][els][ells] < d_mean:
                                f[el][els][ells] = 25
                        elif d[el][els][ells] > d_mean and d[el][els][ells] < d_max:
                                f[el][els][ells] = 75
                        elif d[el][els][ells] == d_mean:
                                f[el][els][ells] = 50
                        elif d[el][els][ells] == d_min:
                                f[el][els][ells] = 0
                        elif d[el][els][ells] == d_max:
                                f[el][els][ells]  = 100





"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print('\n')
print(f"array of f is \n {f}")

# NOTA No he encontrado la razón por la que un valor del array sale 0. Deberían estar todos los valores rellenos
"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

for el in range(2):
        for els in range(3):
                for ells in range(5):
                        if d[el][els][ells] > d_min and d[el][els][ells] < d_mean:
                                f[el][els][ells] = 'C'
                        elif d[el][els][ells] > d_mean and d[el][els][ells] < d_max:
                                f[el][els][ells] = 'D'
                        elif d[el][els][ells] == d_mean:
                                f[el][els][ells] = 'B'
                        elif d[el][els][ells] == d_min:
                                f[el][els][ells] = 'A'
                        elif d[el][els][ells] == d_max:
                                f[el][els][ells]  = 'E'

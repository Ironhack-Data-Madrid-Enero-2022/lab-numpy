#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())
print('_____________________________________')
print('_____________________________________')

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a",
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random(size=(2,3,5)) # La mas facil
a_1 = np.array([[[np.random.random() for i in range(5)]for ii in range(3)]for iii in range(2)]) # Usando list comprehension

# can't thing of a third way 

#4. Print a.
print(a)
print(a_1)

print('_____________________________________')
print('_____________________________________')
#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones(shape=(5,2,3))


#6. Print b.
print(b)
print('_____________________________________')
print('_____________________________________')

#7. Do a and b have the same size? How do you prove that in Python code?
# They have diferents shapes but should have the same size, let's check it,
if a.size == b.size:
        print('a and b have the same size.')
else:
        print('They have different size')

print('_____________________________________')
print('_____________________________________')

#8. Are you able to add a and b? Why or why not?
# No, they have different shapes so you shouldn't be able to add a and b,
try: 
        print('a+b= ' , a+b)
except ValueError:
        print(f'Can not add a and b as they have different shapes. Shape of a: {a.shape}, shape of b: {b.shape}.')
print('_____________________________________')
print('_____________________________________')
#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = b.transpose(1,2,0) 

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
try: 
        d = a+c
        print('a+c= ', d) # now we can add them as they have the same shape 
except ValueError:
        print(f'Can not add a and c as they have different shapes. Shape of a: {a.shape}, shape of c: {c.shape}.')

print('_____________________________________')
print('_____________________________________')
#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print( 'a: ', a)
print('_____________________________________')
print( 'd: ', d)

print('_____________________________________')
print('_____________________________________')
#12. Multiply a and c. Assign the result to e.
e = a*c


#13. Does e equal to a? Why or why not? 
# They should be equal, yes, as c is an array of 1ns, so it should not alter the original matrix
print( 'a: ', a)
print('_____________________________________')
print( 'e: ', e)

print('_____________________________________')
print('_____________________________________')

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty(shape=(2,3,5))

#16. Populate the values in f. For each value in d, 
# If it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
i , j, k = -1 , -1 , -1 
for Dim1 in d:
        i += 1
        for  Dim2 in Dim1:
                j += 1
                for ele in Dim2:
                        k += 1
                        if d_min < ele < d_mean:
                                f[i][j][k] = 25
                        elif d_mean < ele < d_max:
                                f[i][j][k] = 75
                        elif ele == d_mean:
                                f[i][j][k] = 50 
                        elif ele == d_min:
                                f[i][j][k] = 0
                        elif ele == d_max:
                                f[i][j][k] = 100
                k = -1
        j = -1

#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.





#17. Print d and f. Do you have your expected f?
print('Values used to create f: ', d_min, d_max, d_mean)
print('_____________________________________')

print( 'd: ', d)
print('_____________________________________')
print( 'f: ', f)

print('_____________________________________')
print('_____________________________________')
print('The results are as expected!!! Yaaaaay')
# We can observe the expected results! Noooice 
"""For instance, if your d is:
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
r = np.empty(shape=(2,3,5))
r = r.tolist() # OOOOOJO! We have to convert the array into a list or it won't be able to write letters in it. 
i , j, k = -1 , -1 , -1 
for Dim1 in d:
        i += 1
        for  Dim2 in Dim1:
                j += 1
                for ele in Dim2:
                        k += 1
                        if d_min < ele < d_mean:
                                r[i][j][k] = "B"
                        elif d_mean < ele < d_max:
                                r[i][j][k] = "D"
                        elif ele == d_mean:
                                r[i][j][k] = "C" 
                        elif ele == d_min:
                                r[i][j][k] = "A"
                        elif ele == d_max:
                                r[i][j][k] = "E"
                k = -1
        j = -1


print('_____________________________________')

print( 'f: ', f)
print('_____________________________________')
print( 'letter matrix: ', r)

print('_____________________________________')
print('_____________________________________')
print('The results are as expected!!! Yaaaaay')
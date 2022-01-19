#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(f"np.version.version")

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))

#4. Print a.
print(f"a es: {a}")


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.random.randint(1,2,size=(5,2,3))


#6. Print b.
print(f"b es: {b}")


#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size)
print(b.size)
# Si que tienen el mismo tamaño


#8. Are you able to add a and b? Why or why not?

#np.add(a,b)
#-- No se puede debido a este error,ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)
print(f"c es: {c}")

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
#Ahora si se puede por que son del mismo size


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(f"a es: {a}")
print(f"d es: {d}")
#a es el original y d es la suma de a + b.transposed


#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
#e = a*c

#13. Does e equal to a? Why or why not?

print(f"e es: {e}")

#Si, ahora son iguales pues e es igual a*b.transpose y b es un array de solo unos

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min= np.min(d)
d_mean=np.mean(d)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5),int)
print(f"es original f{f}")


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in range(2):
        for j in range(3):
                for k in range(5):
                        if d[i][j][k] > d.min() and d[i][j][k] < d.mean():
                                f[i][j][k] = 25
                        elif d[i][j][k] > d.mean() and d[i][j][k] < d.max():
                                f[i][j][k] = 75
                        elif d[i][j][k] == d.mean():
                                f[i][j][k] = 50 
                        elif d[i][j][k] == d.min():
                                f[i][j][k] = 0
                        elif d[i][j][k] == d.max():
                                f[i][j][k] = 100
print(f"es F {f}")


"""
#17. Print d and f. Do you have your expected f?

"""
print(f"es a {a}")
print(f"es a {f}")
#Obtengo lo esperado


#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 

L = np.empty((2,3,5),str)
for i in range(2):
        for j in range(3):
                for k in range(5):
                        if d[i][j][k] > d.min() and d[i][j][k] < d.mean():
                                L[i][j][k] = 'B'
                        elif d[i][j][k] > d.mean() and d[i][j][k] < d.max():
                                L[i][j][k] ='D'
                        elif d[i][j][k] == d.mean():
                                L[i][j][k] = 'C'
                        elif d[i][j][k] == d.min():
                                L[i][j][k] = 'A'
                        elif d[i][j][k] == d.max():
                                L[i][j][k] = 'E'
print(f"es F {L}")
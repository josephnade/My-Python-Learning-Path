import numpy as np

#1-) Create an array includes (10,15,30,45,60) numbers.
np_array1 = np.array([10,15,30,45,60])
print(np_array1)

#2-) Create an array between 5 and 15 numbers.
np_array2 = np.arange(5,16)
print(np_array2)

#3-) Create an array between 50 and 100 but numbers increases 5.
np_array3 = np.arange(5,101,5)
print(np_array3)

#4-) Create an array includes 10 zeros.
np_array4 = np.zeros(10)
print(np_array4)

#5-) Create an array includes 10 ones.
np_array5=np.ones(10)
print(np_array5)

#6-) Create an array between 0 and 100 but 5 same ranges.
np_array6 = np.linspace(0,100,6)
print(np_array6)

#7-) Create an array between 10 and 30 but randomly 5 numbers
np_array7 = np.random.randint(10,31,5)
print(np_array7)

#8-)Create an array between -1 and 1 but randomly 10  float numbers
np_array8 = np.random.randn(10)
print(np_array8)

#9-)Create an array between 10 and 50 randomly but size of 3x3 matrices.
np_array9 = np.random.randint(10,51,9).reshape(3,3)
print(np_array9)

#10-) Calculate row and column sum of np_array9.
sum_of_row_np_array_9 = np_array9.sum(axis = 1)
sum_of_column_np_array_9 = np_array9.sum(axis = 0)
print(sum_of_row_np_array_9)
print(sum_of_column_np_array_9)

#11-) Calculate min,max and avg of np_array9
minimum = np.min(np_array9)
maximum = np.max(np_array9)
average = np.average(np_array9)
print(f"min = {minimum} max = {maximum} average = {average}")

#12-) Find the biggest number index of np_array9
max_index = np.argmax(np_array9)
print(max_index)

#13-) Find first 3 numbers of array that between 10-20.
np_array10 = np.arange(10,21)
print(np_array10[0:3])

#14-) Find reverse of np_array10 array.
print(np_array10[::-1])

#15-) Find the first row of np_array9.
print(np_array9[0])

#16-) Find 2. row and 3. column of np_array9.
print(np_array9[1,2])

#17-) Find the first number in all row of np_array9.
print(np_array9[:,0])

#18-) Find the square of numbers in np_array9.
print(np.square(np_array9))

#19-) Find positive even numbers in np_array9.
even = np_array9[np_array9 % 2 == 0]
result = even[even > 0]
print(result)

#Practical No. 9


import numpy
a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
b = numpy.array([[1,2,4],[3,5,7],[6,8,9]])
c = numpy.array([[1,5,9],[2,3,6],[4,7,8]])
print("The element wise addition of matrix is : ")
print(numpy.add(a, b,c))
print("The element wise subtraction of matrix is : ")
print(numpy.subtract(a, b,c))
print("the element wise multiplication is:")
print(numpy.dot(a,b,c))
print("Transpose of matrix a is:\n",(a.T))
print("Transpose of matrix b is:\n",(b.T))
print("Transpose of matrix c is:\n",(c.T))

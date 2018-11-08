import numpy

a = numpy.arange(12)
print(a)
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
a.transpose()
print(a)

import statistics
array = list()
num = input()
for i in range(int(num)):
    n = input()
    array.append(int(n))
print (array)
array.sort()
print(array)
print(statistics.median(array))

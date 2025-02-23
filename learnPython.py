import numpy as np

l=list(range(1,21))
print(f"First 20 numbers {l}")

l=l[1:len(l):2]

print(f"Sliced even number {l}")

l+=list(range(22,51,2))
print(f"Added list to find even number till 50 {l}")

l.sort()
print(f"Sorted {l}")
med=np.median(l)

print(f"Median : {med}")

i=int(input("Enter length"))
j=0
l=[]

while j<i:
    l.append(int(input()))
    j+=1

print(f"List is {l}")
length=len(l)
custom_median=0
if length%2==0:
    custom_median=(l[int(length/2)]+l[(int(length/2))-1])/2
else:
    custom_median=l[int(length/2)]
print(f"CustomMedian {custom_median}")
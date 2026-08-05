# Mutable : change of any value is allowed 
# duplicat : there can be multiple Value
# ordered : elements can be accessed in the same order as they are inserted by index value 
# heterogenous : allow to store multiple datatype in a single list 


a = [12 , 13, 14 , 15, 16, 34.5 ]

# print(a[0:5])
# print(a[::-1])
# print(a[-2])

# print(len(a))

# 1st way using index

for i in range(len(a)):
    print(a[i])

# 2nd way using direclty on value 

for i in a:
    print(i)


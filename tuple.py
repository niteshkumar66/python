# Tupple 

# immutable : value cannot be modified after creation
# duplicate : there can be multiple same Value 
# ordered : elements can be accessed in the same order as they are inserted by index value 
# heterogenous : allow to store multiple datatype in a single list  


a = (1,2,3,4,3,4,7,3,8,9,2,3)
# print(type (a))


# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])


# print(a.index(4))
# print(a.count(3))



# a,b,c,d = (1,2,3,4)       # value of tuple getting unpacked to a = 1 , b = 2 , c = 3 , d = 4
# print(a)
# print(b)
# print(c)
# print(d)


a = (1)                     # consider as int => because of tuple unpacking 
print(type(a))

a = (1,)                    # it is considered as tuple because of comma (,)
print(type(a))
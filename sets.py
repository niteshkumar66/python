# SETS

# Mutable : change of any value is allowed 
# duplicate : there can be multiple same Value 
# Unordered : elements cannot be accessed by index value 
# semi-heterogenous : it can store some different datatypes (string , number, tuples ) but not all 

# s = {1,2,9,3,"hello",4,5,6,5}

# for i in s:
#     print(i)

# print(s)

# print(hash("Nitesh"))

# set methods 

# a = {1,2,3,5,7,9}
# b = {3,5,2,4,6,8,}

# a.remove(3)                           # raise error if element not found
# a.discard(3)                          # raise no error if element not found
# a.pop()                               # it pop the value which has least hash value from the set 
# a.clear()                             # remove all the elements

# a.add(2)                              # add value to the set 

c = a.union(b)                        # c = a|b
# c = a.intersection(b)                 # c = a & b
# c = a.difference(b)                   # c = a-b
# c = b.difference(a)                   # c = b-a
# c = a.symmetric_difference(b)         # c = a ^ b

# print(c)
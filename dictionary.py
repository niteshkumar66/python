# Dictonary

# Mutable : Semi Mutable , keys can't be change but the value can be changed 
# Duplicate : Key must be unique but the value can be duplicate (same)
# Ordered : Dictonary follows insertion order
# heterogenous : allow to store multiple datatype in a single list  


# d = {}
# print(type(d))

# a = {
#     1: "Hello",
#     "name": "Nitesh Kumar",
#     "age" : 23
# }

# print(a)
# print(a["name"])


d = {1: 100, 2: 200 , 3: 300, 4: 400}

# d[1] = 1000
# d.update({50: 500})       # Updating 
# d[50] = 500                 # Creating 
# del d[2]                    # Deleting 

# print(d)


# for i in d:
#     print(d[i])

# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)

# d.clear()                 # clear the all key and value

# d2 = d.copy()               # create a shallow copy the dictonary
# del d2[3]

# print(d)

# print(d.get(2))
                        # both are same 
# print(d[2])

# print(d.items())

# d1 = d.pop(2)             # pop the key from the dictornary and return the value to other variable
# print(d)
# print(d1)

# d1 = d.popitem()          # pop the last key from the dictonary and return the key value pair to other variable
# print(d)
# print(d1)

# help(dict)
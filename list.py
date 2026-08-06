# Mutable : change of any value is allowed 
# duplicat : there can be multiple same Value 
# ordered : elements can be accessed in the same order as they are inserted by index value 
# heterogenous : allow to store multiple datatype in a single list 


a = [12 , 13, 14 , 15, 16, 34.5 ]

# print(a[0:5])
# print(a[::-1])
# print(a[-2])

# print(len(a))

# 1st way using index

# for i in range(len(a)):
#     print(a[i])

# 2nd way using direclty on value 

# for i in a:
#     print(i)


# print(dir(list))
# help(list)


l = [1,2,2,3,4,5,6]
# l.append(6)
# l.append(7)

# l.extend([4,5,6])

# l.insert(1,2)

# pop_item = l.pop(4)
# print(pop_item)

# print(l.index(4))

# print(l.count(2))

# l.reverse()

# m = l.copy()

# l.remove(5)

# print(m)


# l[0] = 10
# print(l)

#print positive and negative number of list

# li = [1, -4, 5, -10, -21, 45]
# pos_li = []
# neg_li = []

# for i in range (len(li)):
#     if (li[i] >= 0 ):
#         pos_li.append(li[i])
#     else :
#         neg_li.append(li[i])

# print(f"Positive Numbers are {pos_li}")
# print(f"Negative Numbers are {neg_li}")


# mean of the list 

# a = [1,4,5,7,8,19,34]
# sum = 0
# for i in a :
#     sum += i

# print(sum/len(a))


# find the greatest element and print its index too

# a = [2,4,6,8,16,12,14]
# max = a[0]
# index = 0

# for i in range(1, len(a)):
#     if (a[i] > max):
#         max = a[i]
#         index = i


# print(f"maximum value is {max} at the index {index}")

# find the second largest number of the list

# a = [2,5,10,3,19,17]
# max = a[0]
# sec_max = a[0]

# for i in a:
#     if i > max:
#         sec_max = max
#         max = i
#     elif i > sec_max:
#         sec_max = i

# print(f"maximum value is {max} and second maximum value is {sec_max}")


# check if the list is sorted or not 

# a = [1,2,3,4,5]
a = [2,5,10,3,19,17]
# max = a[0]

# for i in a :
#     if i > max:
#         max = i
#     elif i < max :
#         print("Unsorted List")
#         break

# else : 
#     print("Sorted List")

#effective approach 

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else : 
        print("Unsorted List")
        break
else : 
    print("Sorted List")
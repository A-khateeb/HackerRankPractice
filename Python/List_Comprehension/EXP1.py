# h_letter = []
# for i in 'human':
#     h_letter.append(i)
#
# print(h_letter)


# i = int(input("Insert value X:\t"))
# j = int(input("Insert value Y:\t"))
# k = int(input("Insert value Z:\t"))
# n = int(input("Insert value N:\t"))
# for x in range(0,i):
#     print(x)
#     for y in range(0,j):
#         print(x,y)
#         for z in range(0,k):
#             print(x,y,z)
# if (x+y+z) != n:
#     print("true")
# elif (x+y+z) == n :
#     print("false")

i = int(input("Insert value X:\t"))
j = int(input("Insert value Y:\t"))
k = int(input("Insert value Z:\t"))
n = int(input("Insert value N:\t"))

i += 1
j += 1
k += 1

tmp_list = [[x,y,z] for x in range(i) for y in range(j) for z in range(k) if x+y+z != n]
print(tmp_list)

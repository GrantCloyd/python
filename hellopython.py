# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:  
#         print(f"{num} is even")
#     else: 
#         print(f"{num} is odd")     

# row = 1
# while row <= 10:
#     print("\U0001f600" * row)
#     row +=1

# working with slice functionality

# tasks = ["Drat", "Comedy", "You Fools", "ARRR", "HEIM!"]


# print(tasks[1:])
# print(tasks[:-1])
# print(tasks[::-2])

# working with list comprehension

# num_list = [1,2,3,4, 5, 6]


# print([val * 10 for val in num_list])

# name = "Grant"

# print("".join([char.upper() for char in name]))

# evens = [] 
# odds = []
# [evens.append(num) if num %2 == 0  else odds.append(num) for num in num_list ]

# print(evens)
# print(odds)

# nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# [[print(val) for val in lis] for lis in nested_list]

# inner_loop = ['X' if col % 2 != 0 else 'O' for col in range(1,5)]

# print([inner_loop for row in range(1,5)])

# print([['X' if col % 2 != 0 else 'O' for col in range(1,5)] for row in range(1,5)])
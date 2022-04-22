# fibonacci series between 0 to 50
# x, y = 0, 1

# while y < 50:
#     print(y)
#     x, y = y, x+y

# Fizzbuzz for loop
# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("Fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("Buzz")
#         continue
#     print(fizzbuzz)

# print numbers in range expect 3 and 6
# for x in range(6):
#     if (x == 3 or x == 6):
#         continue
#     print(x, end=" ")
#     print("\n")

# write python conditional that generates a two-dimensional array
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row*col
print(multi_list)

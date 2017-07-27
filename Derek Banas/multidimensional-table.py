# ---------- PROBLEM : CREATE MULTIPLICATION TABLE ----------
# With 2 for loops fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''
 
# Create the multidimensional list
multi_table = [[0]* 10 for i in range(10)]

# This will increment for each row
for i in range(1, 10):

    # This will increment for each item in the row
    for j in range(1, 10):
 
        # Assign the value to the cell
        multi_table[i][j] = i * j
 
# Output the data in the same way you assigned it
for i in range(1, 10):
    
        for j in range(1, 10):
            print(multi_table[i][j], end=", ")

        print()

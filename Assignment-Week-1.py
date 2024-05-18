def lower_triangular(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def upper_triangular(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

def pyramid(levels):
    for i in range(levels):
        print(' ' * (levels - i - 1) + '* ' * (i + 1))

rows = int(input("Enter Number of Rows: "))
levels = int(input("Enter Number of Levels: ")) 

print("Lower Triangular Pattern:")
lower_triangular(rows)

print("\nUpper Triangular Pattern:")
upper_triangular(rows)

print("\nPyramid Pattern:")
pyramid(levels)

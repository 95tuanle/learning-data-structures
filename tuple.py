point = (5, 2)

x = point[0]
y = point[1]


def calculate_square_properties(side_length):
    area = side_length ** 2
    perimeter = side_length * 4
    return area, perimeter


result = calculate_square_properties(5)
print("Area:", result[0])
print("Perimeter:", result[1])

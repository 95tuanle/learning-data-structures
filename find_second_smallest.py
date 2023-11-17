def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]


def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = min(my_list[0], my_list[1])
    second_smallest = max(my_list[0], my_list[1])
    for element in my_list[2:]:
        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif element < second_smallest:
            second_smallest = element
    return second_smallest


def find_second_smallest_v3(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for element in my_list:
        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif element < second_smallest:
            second_smallest = element
    return second_smallest


print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))
print(find_second_smallest_v3([5, 8, 3, 2, 6]))

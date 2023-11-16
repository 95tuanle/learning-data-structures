student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

student_pet_count_list[2] = 3
print(student_pet_count_list[2])
student_pet_count_list[3] += 1
print(student_pet_count_list[3])
student_pet_count_list[-1] += 2
print(student_pet_count_list[-1])

student_pet_count_list.append(4)
print(student_pet_count_list[-1])

ITEM_AT_INDEX_THREE = student_pet_count_list[3]
# print(student_pet_count_list[100])
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM += INDIVIDUAL_PET_COUNT
print(SUM)

AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)
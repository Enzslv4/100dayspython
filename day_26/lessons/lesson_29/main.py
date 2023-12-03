with open('day_26/lesson/lesson_29/file1.txt') as file1:
    str_nums_1 = file1.readlines()
    nums_1 = [int(num.split()) for num in str_nums_1]

with open('day_26/lesson/lesson_29/file2.txt') as file2:
    str_nums_2 = file2.readlines()
    nums_2 = [int(num.split()) for num in str_nums_2]

common_nums = [num.split() for num in nums_1 if num in nums_2]

print(common_nums)
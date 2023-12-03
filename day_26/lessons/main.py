# list comprehension

import random
import pandas

'''
num_l = [1,2,3,4,5]
new_list = [item + 1 for item in num_l]

name = 'Enzo'
letters_list = [letter.upper() for letter in name]
print(letters_list)

test = True

numbers = [num * 2 for num in range(1,5) if test]
print(numbers)
'''

'''
names = ['Enzo', 'Henrique', 'Ana', 'Jonathan', 'Pedro']
short_names = [name for name in names if len(name) < 5]
caps_names = [name.upper() for name in names if name not in short_names]
print(short_names, caps_names)
'''

# lesson 27:

'''
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [num ** 2 for num in nums]
print(squared_nums)
'''

# lesson 28(odd or even)

'''
nums = [num for num in range(1, 100) if num % 2 == 0]
print(nums)
'''

# lesson 31
#   new_dict = {new_key:new_value for item in list} for a dict based on a alread exiting list
#   new_dict = {new_key:new_value for (key,value) in dict.items()} using another dict as a base

'''
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {name:random.randint(0, 10) for name in names}

passed_students = {name:score for (name,score) in students_scores.items() if score > 5}

print(students_scores)
print(passed_students)
'''

students_dict = {
    'students': ['Angela', 'James', 'Lily'],
    'scores': [56, 76, 98]
}

students_data_frame = pandas.DataFrame(students_dict)

# To loop through rows of a data frame

for (index, row) in students_data_frame.iterrows():
    print(row.students)
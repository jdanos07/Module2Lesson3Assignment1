#Task 2: Calculate the average grade and print it.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = (sum(grades)/(len(grades)))
print(average)

#Didn't specify whether it should be an int or a flt.
#I certain this is what was intended:

grades.sort()
middle_index = len(grades) // 2
avg = grades[middle_index]
print(avg)

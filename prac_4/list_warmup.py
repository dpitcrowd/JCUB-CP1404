"""
Create a Python file called lists_warmup.py and enter the following line:

numbers = [3, 1, 4, 1, 5, 9, 2]

What values do the following expressions have?
Without running the code, write down your answers to these questions
(on paper, or in your Python file as a comment),
then use Python to see if you were correct.

[3, 1, 4, 1, 5, 9, 2]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])

for n in numbers:
    if n == 5:
        print(n)
    elif n == 9:
        print(n)
    elif n == "3":
        print(n)

numbers.append([6, 5, 3])
print(numbers, "\n")

"""Write Python expressions (in the same Python file) to achieve the following:"""

#Change the first element of numbers to "ten" (the string, not the number 10)
print('Change the first element of numbers to "ten" (the string, not the number 10)', "\n",
      numbers)
numbers[0] = "ten"
print(numbers[0])
print(numbers, "\n")

#Change the last element of numbers to 1
print('Change the last element of numbers to 1', "\n", numbers)
numbers[len(numbers)-1] = 1
print(numbers)

#Get all the elements from numbers except the first two (slice)
print('Get all the elements from numbers except the first two (slice)', "\n", numbers)
print(numbers[2:], '\n')

#Check if 9 is an element of numbers
print('Check if 9 is an element of numbers')
print(numbers)
counter = 0
for n in numbers:
    counter += 1
    if n == 9:
        print('Number {} is into the list and is at {}th position \n'.format(n, counter))





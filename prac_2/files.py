""" Append user name in name.txt file"""
#out_file = open("name.txt", "a")
#name = input("Enter your name please --> ")
#print("{}".format(name).lower(), file=out_file)
#out_file.close()

""" Use read() to gather data from a file"""
#temp_file = open("name.txt", "r")
# Show the entire text
#print("Your name is", temp_file.read())
#temp_file.close()

""" Use readline() to gather data from a file"""
#temp_file = open("name.txt", "r")
# Show a single line at the time
#print("Your name is", temp_file.readline())
#temp_file.close()

""" Use readlines() to gather data from a file"""
#temp_file= open("name.txt", "r")
# Read the whole file and split it by line
#print("Your name is", temp_file.readlines())
#temp_file.close()

""" Use FOR LOOP to gather data from a file"""
#temp_file = open("name.txt", "r")
#
#for line in temp_file:
    #print("Your name is", line)
#temp_file.close()

""" Read numbers.txt file"""
my_list = []
def my_add(a, b):
    add = a + b
    return add
temp_file =open("numbers.txt", "r")
for line in temp_file:
    my_list.append(line)
a = int(my_list[0])
b = int(my_list[1])

print("The sum of the first two number is ", my_add(a,b))
temp_file.close()

""" Count the total of the lines in a file and to sum them"""
my_list_read = []
tot = 0
try:
    temp_file = open("numbers.txt", "r")
    for line in temp_file:
        my_list_read.append(line)
    temp_file.close()

    temp_file = open("numbers.txt", "r")
    for line in temp_file:
        num = int(line)
        tot += num
    temp_file.close()
    print("The total number of the rows is {}, and their sum is {:.2f}".format(len(my_list_read), tot))
except:
    print("File doesn't exit !!!")
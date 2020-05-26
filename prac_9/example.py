"""
Write a  program to determine which is the
largest  file in the current directory, as
defined  by  total number of characters in
the file. You will need to use the os module.
"""
import os
#os.getcwd()


def main():
    my_dir = '/home/davide/PycharmProjects/JCUB-CP1404/prac_8/'
    #my_files = os.listdir('../')
    my_files = os.listdir(my_dir)
    the_largest = 0
    file_size_list = []

    for file in my_files:
        print(file)

    os.chdir(my_dir)
    for i in os.listdir(os.curdir):
        if os.path.isfile(i):
            file_size_list.append((i, os.path.getsize(i)))

    for file_name, file_size in file_size_list:
        if file_size > the_largest:
            the_largest = file_size
            largest_file = file_name

    print(largest_file, the_largest)


if __name__ == '__main__':
    main()
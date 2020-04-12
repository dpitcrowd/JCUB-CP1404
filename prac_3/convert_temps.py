"""
More temperatures Create a text file called temps_input.txt and fill it with at least 15 floats of any values between
-200 and +200. Where will you get these numbers from?
Write a Python script to create the text file, of course!

Now write a program, convert_temps.py , that uses the functions you made to convert temperatures.
Read the values in temps_input.txt as Fahrenheit values and write the converted Celsius values to temps_output.txt.
"""


def input_file():
    import random
    temps_input = open("temps_input.txt", "w")
    for i in range(15):
        temp = random.uniform(-200.00, 200.00)
        print("{}".format(temp), file=temps_input)
    temps_input.close()


def ext_file():
    my_ext_file = open("temps_input.txt", "r")
    for fahrenheit in my_ext_file.readlines():
        convert_celsius(fahrenheit)


def convert_celsius(fahrenheit):
    """ Convert Fahrenheit degrees in Celsius degrees"""
    celsius = (float(fahrenheit) - 32) / (9.0 / 5)
    output_file(celsius)


def output_file(celsius):
    temps_output = open("temps_output.txt", "a")
    print(celsius, file=temps_output)
    temps_output.close()


def main():
    """ Run my script"""
    input_file()
    ext_file()


main()
#Started: May 14,2023

#To run the code in python line, press **** shift + enter ****, to run the code in python file, press **** F5 ****

#Everytime that you want to find out about an error you are getting, you can copy and search it in google.
#We can use # to comment in python. Also, if we want to comment a block of code, we can use ''' or """ at the beginning and end of the block of code. Also, we can use ctrl + / to comment a block of code.

#It's important to write our code in a way that it can be readable, clear and understandable. Also, we should use meaningful names for our variables.
#We can not use space between names. We can use underscore instead of space.
#We can not use python keywords as a variable name. for example: print, input, len, etc.
#We can not use numbers at the beginning of the variable name. But we can use numbers in the middle or at the end of the variable name. 

print("Hello World!") #whole line is a statement. print is a function. Hello World! is an argument. we can have multiple arguments in a function. we call it a code block.

#It will print everything in the brackets.
#string is a sequence of characters(like a text), it is always in quotes.
#we can use single quotes or double quotes. but if we have a single quote in the string, we have to use double quotes and vice versa. Also we can use triple quotes.

print('Hello World!\nHello World!')
# \n is used to print the next line. Also when we want the corsor to go to the next line, when we are gathering info from the user, we can use \n.

print('Hello' + ' ' + 'Ehsan')

input('a prompt for the user: ')
#it will print the prompt and wait for the user to enter something. After the user entered the answer, this answer will be replaced by that statement(code).

print('Hello' + ' ' + input('What is your name? '))
#we can use input function inside the print function. it will print the prompt and wait for the user to enter something. After the user entered the answer, this answer will be replaced by that statement(code). Then it will print the rest of the statement.

print(len(input('What is your name?')))
#len is a function that will count the number of characters in the string. it will print the prompt and wait for the user to enter something. After the user entered the answer, this answer will be replaced by that statement(code). Then len will count the number of characters in the string and will be replaced by the number of characters. then print functuion will print the rest of the statement.

name = input('What is your name? ')
length = len(name)
print(length)
#Variable is a box that we can store something in it. we can use this box later in the code. we can change the content of the box later in the code.
#we can use the variable name in the code instead of the content of the box.
#Variables are case sensitive. name and Name are different variables.
#Variables are iterable. we can use the content of the box in the code, and Changeable. we can change the content of the box later in the code.

temp = name
name = length
length = temp
print(name,length)
#By using this code, we can swap the content of the boxes.



      
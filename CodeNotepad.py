#Started: May 24,2023

#To run the code in python line, type python3 in bash or press **** shift + enter ****, to run the code in python file, press **** F5 ****
#We can add a python file to the bash by typing **** python3 filename.py ****

#Python is Dynamically typed. It means that we don't have to specify the type of the variable. We can change the type of the variable later in the code. for example: x = 123, x = 'Ehsan', etc.
#But for example C++ is Statically typed. It means that we have to specify the type of the variable. for example: int x = 123, string x = 'Ehsan', etc.

#Everytime that you want to find out about an error you are getting, you can copy and search it in google.
#We can use # to comment in python. Also, if we want to comment a block of code, we can use ''' or """ at the beginning and end of the block of code. Also, we can use ctrl + / to comment a block of code.

#---------------------------------------------How to write codes-------------------------------------------

#It's important to write our code in a way that it can be readable, clear and understandable. Also, we should use meaningful names for our variables.
#1-We can not use space between names. We can use underscore instead of space.
#2-We can not use python keywords as a variable name. for example: print, input, len, etc.
#3-We can not use numbers at the beginning of the variable name. But we can use numbers in the middle or at the end of the variable name.
#4-We can not use special characters in the variable name. for example: !, @, #, $, %, ^, &, *, etc.
#5-Most of the time, we use lowercase for variable names.
#6-the most common way to name a variable is to use lowercase and underscore(snake case). for example: my_name, my_age, etc. and if we want to use numbers, we have to use them at the end of the variable name. for example: my_name1, my_age2, etc.
#7-There are few cases that we use uppercase for variable names. for example: PI, URL, etc. for values that we know that they are not going to change.
#8-We can use UpperCamelCase for class names. for example: MyClass, etc.
#9-Double underscore at the beginning of the variable name is used for private variables. for example: __name, etc.
#10-Double underscore at the beginning and end of the variable name is used for special methods. for example: __init__, etc.Stuff that we should not touch.

#---------------------------------------------Type&Print-------------------------------------------

type(123) #it will tell us the type of the variable. for example: int, float, string, etc.
#Outcome of adding an integer and a float is a float.

print("Hello World!") #whole line is a statement. print is a function. Hello World! is an argument. we can have multiple arguments in a function. we call it a code block.
# operater is a symbol that tells the computer to perform a specific mathematical or logical manipulation. for example: +, -, *, /, etc.
# operand is a term used to describe any object that is manipulated by an operator. for example: 2 + 3, 2 and 3 are operands and + is an operator.
# expression is a combination of values, variables, operators, and calls to functions.
# statement is a unit of code that the Python interpreter can execute. for example: print("Hello World!"), x = 1, etc.
# function is a block of code which only runs when it is called. for example: print(), input(), len(), etc.
# argument is the value that we pass to the function when we call that function. for example: print("Hello World!"), "Hello World!" is an argument.
#value is a piece of data that we can store in a variable. for example: 123, 3.14, "Hello World!", etc.

#It will print everything in the brackets.
#string is a sequence of characters(like a text), it is always in quotes.
#we can use single quotes or double quotes. but if we have a single quote in the string, we have to use double quotes and vice versa. Also we can use triple quotes.

print('Hello World!\nHello World!')
# \n is used to print the next line. Also when we want the corsor to go to the next line, when we are gathering info from the user, we can use \n.
print('Hello World!\\Hello World!')# \\ is used to print a back slash\.

print('Hello' + ' ' + 'Ehsan')

#---------------------------------------------Variables-------------------------------------------

#Variable is a box that we can store something in it. we can use this box later in the code. we can change the content of the box later in the code.
#we can use the variable name in the code instead of the content of the box.
x = 123 #we can assign a value to a variable by using =. we can change the value of the variable later in the code.
new_name = 'Ehsan' #we can use underscore instead of space.
#Variables are case sensitive. name and Name are different variables.
#Variables are iterable. we can use the content of the box repeatedly in the code, and Changeable. we can change the content of the box later in the code.***It means that  we can reassign a value to a variable.***
#Variables can be assigned to other variables.****
all, at, once = 5, 10, 15 #we can assign multiple variables at once.
num_of_friends = 5
num_of_friends = 8 #we can reassign a value to a variable.
num_of_friends = num_of_friends + 1 #we can use the content of the box in the code.
num_of_friends += 1 #we can use += to add 1 to the content of the box.
num_of_friends -= 1 #we can use -= to subtract 1 from the content of the box.
num_of_friends *= 2 #we can use *= to multiply the content of the box by 2.
num_of_friends /= 2 #we can use /= to divide the content of the box by 2.
friends = num_of_friends #we can assign a variable to another variable.

#-----------------------------------------Most common Data types----------------------------------------

#int is a whole number. for example: 123, 0, -123, etc.
#float is a number with a decimal point. for example: 3.14, 0.0, -3.14, etc.
#str is a string. for example: 'Hello World!', '123', etc.***It is always in quotes.***
#bool is a boolean. for example: True, False, etc.***It is always in capital letters without any paratheses or... .***
#list is a collection of items. for example: [1, 2, 3], ['a', 'b', 'c'], [1, 'a', True], etc.***It is always in square brackets.***
#dict is a dictionary. A collection of key values. for example: {'name': 'Ehsan', 'age': 30}, etc.***It is always in curly brackets.***
#None is a special data type. it means nothing. for example: None, etc. we can set a variable to None. for example: x = None, etc.

#----------------------------------------------String-----------------------------------------------------

#string is a sequence of characters(like a text), it is always in quotes.
#we can use single quotes or double quotes. but if we have a single quote in the string, we have to use double quotes and vice versa. Also we can use triple quotes.
#we can use any character in the string.
#If we want to make a whole paragraph, we can use triple quotes. we can use single quotes or double quotes inside the triple quotes.
name = 'Ehsan@sh'
name = 'Ehsan' +' '+ '@sh'
#Concatenation is used to combine two strings. we can use + to concatenate two strings.
#We can not concatenate a string and a number. we have to convert the number to a string first.
name = 'Ehsan' + ' ' + str(30)
#We can use str() to convert a number to a string.
name = 'Ehsan' * 3
#We can use * to repeat a string.
name = 'Ehsan'
name += 'Ash'
#We can use += to concatenate two strings. Instead of name = name + 'Ash'.

#***********
name = 'Ehsan'
guess = 7
print(f'Hello {name}! Your guess is {guess}.')
# f string
#We can use + to concatenate two strings. But we can not concatenate a string and a number. we have to convert the number to a string first.
#interpolation is used to put a variable inside a string. we can use f to format a string. we can use {} to put a variable inside the string.
#We call a variable inside a string, a placeholder.
print('Hello {}! Your guess is {}.'.format(name, guess))#The older way to format a string.
print(name+' '+str(guess))#The older way to concatenate two strings.


#----------------------------------------------Input-----------------------------------------------------

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



      
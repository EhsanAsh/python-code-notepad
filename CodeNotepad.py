#Started: May 24,2023

#To run the code in python line, type python3 <file-name>(you should be in the same directory or mention the directory) in bash , to run the code in python file, press **** Ctrl+F5 **** To exit the python line, type **** quit() or Ctrl+z+Enter****to open a python command line type python3 in teminal****to open a vscode file in the bash, type **** code . filename.py ****to open a python file in the bash, type **** python3 filename.py ****

#To break a while loop, when we are running the code in python line, we can press Ctrl+c.

#Python is incredibly versatile and can be used for everything from web development to data science to machine learning.

#Python is Dynamically typed. It means that we don't have to specify the type of the variable. We can change the type of the variable later in the code. for example: x = 123, x = 'Ehsan', etc.
#But for example C++ is Statically typed. It means that we have to specify the type of the variable. for example: int x = 123, string x = 'Ehsan', etc.

#Everytime that you want to find out about an error you are getting, you can copy and search it in google.

#We can use # to comment in python.  Also, we can use ctrl + / to comment a block of code.

#---------------------------------------Python Components-------------------------------

#Python, like many other programming languages, is composed of various components and parts. Here are some key components:

#Variables: Variables are containers for storing data values. In Python, variables do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned to a variable.

#Data Types: Python has several built-in data types. These include integers (int), floating point numbers (float), complex numbers (complex), strings (str), lists (list), tuples (tuple), dictionaries (dict), and sets (set).

#Operators: Operators are used to perform operations on variables and values. Python includes arithmetic operators (+, -, *, /, %, **, //), comparison operators (==, !=, >, <, >=, <=), assignment operators (=, +=, -=, *=, /=, etc.), logical operators (and, or, not), and more.

#Statement: A statement in Python is a logical instruction which the Python interpreter can read and execute. In simple terms, a statement is a single line of code that performs a specific task. Examples of statements include assignment statements like x = 5, control flow statements like if, for, while, function definitions, and more.

#Expression: An expression is a combination of values, variables, operators, and function calls, which are evaluated by Python's interpreter to produce a value. Examples include 2 + 2, x * y, len("hello"). The key point is that expressions are evaluated to a value.

#Value: A value is the most basic form of data that a program works with. It could be a number (like 5, 10.5), a string ("Hello World"), a list ([1, 2, 3]), or many other things. Values belong to different data types: 2 is an integer, Hello, World! is a string, etc.

#Argument: An argument (or parameter) is a value that is passed to a function or method when it is called. For example, in len("hello"), "hello" is an argument being passed to the len function. Arguments are essentially inputs to functions and methods which they use to perform their tasks.

#Control Flow: This includes if-else statements, while loops, and for loops, which allow the code to make decisions and repeat actions.

#Functions: Functions are reusable pieces of code that perform a specific task. You can define your own functions using the def keyword, and Python has a number of built-in functions like print(), len(), etc.

#Methods: Methods are like functions, but they're associated with object/classes. Methods in objects are functions that belong to the object.

#Classes and Objects: Python is an object-oriented programming language. You can define your own objects using classes, which can have their own attributes and methods.

#Modules and Packages: Modules are pieces of code that you can import into your program. A package is a way of organizing related modules into a directory hierarchy.

#Exceptions: Exceptions are events that occur during the execution of a program that disrupt the normal flow of a program's instructions. Python has several built-in exceptions that can be handled with try/except statements, and you can define your own.

#Decorators: Decorators allow you to wrap a function or method in another function that can add functionality, modify arguments or results, etc.

#Generators: Generators are a type of iterable, like lists or tuples. Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops. They are created using functions and the yield statement.

#List Comprehensions: Python supports list comprehensions, which provide a concise way to create lists based on existing lists.

#Context Managers: Context managers allow setup and cleanup actions to be taken for objects when their creation and destruction times are not predictable. They're created using the with statement.

#AsyncIO: This is a library to write single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.

#File I/O: Python has several functions for creating, reading, writing, and deleting files.

#These are just some of the components and parts of Python. 

#------------------------------------How to write codes----------------------------------

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

#----------------------------------------Type&Print-------------------------------------

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
#we can use single quotes or double quotes. but if we have a single quote in the string, we have to use double quotes and vice versa. Also we can use triple quotes.

print('Hello World!\nHello World!')
# \n is used to print the next line. Also when we want the corsor to go to the next line, when we are gathering info from the user, we can use \n.
print('Hello World!\\Hello World!')# \\ is used to print a back slash\.

print('Hello' + ' ' + 'Ehsan')

#---------------------------------------------Variables----------------------------------

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

#-----------------------------------Most common Data types------------------------------

#int is a whole number. for example: 123, 0, -123, etc.
#float is a number with a decimal point. for example: 3.14, 0.0, -3.14, etc.
#str is a string. for example: 'Hello World!', '123', etc.***It is always in quotes.***
#bool is a boolean. for example: True, False, etc.***It is always in capital letters without any paratheses or... .***
#list is a collection of items. for example: [1, 2, 3], ['a', 'b', 'c'], [1, 'a', True], etc.***It is always in square brackets.***
#dict is a dictionary. A collection of key values. for example: {'name': 'Ehsan', 'age': 30}, etc.***It is always in curly brackets.***
#None is a special data type. it means nothing. for example: None, etc. we can set a variable to None. for example: x = None, etc.

#----------------------------------------------String------------------------------------

#to have multiline string, we can use triple quotes like this:
a = """Hello. My name is Ehsan. I am 30 years old. I am a software developer. I am learning python. """
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

#to check the length of a string, we can use len() function.

#to access a character in a string, we can use index. index starts from [0].
name = 'Ehsan'
print(name[0]) #it will print E.

#check string:
name = 'My name is Ehsan'
print('Ehsan' in name) #it will return True.

#slicing:
name = 'Ehsan Ashrafipour'
print(name[2:6]) #it will print san. it will start from index 2 and end at index 5. it will not include index 6. 
#we can also use negative numbers. it will start from the end of the string. for example:
print(name[-4:-1])# it will print pou.

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

#----------------String Method ------------------

name = input('What is your name?\n').lower()
# .lower() is a string method. we can use it to convert a string to lowercase.
#.upper() is a string method. we can use it to convert a string to uppercase.
#.capitalize() is a string method. we can use it to capitalize the first letter of a string.

#to remove white spaces from the beginning and the end of a string, we can use .strip() method.
name = ' Ehsan Ash  '
name = name.strip()

#to replace a character in a string, we can use .replace() method.
name = name.replace('a', 'A')

name = name.index('A') #it will return the index of the first character of the string. it will return an error if the character is not in the string.
#syntax: string.index(value, start, end) #start and end are optional.

name = name.find('A') #it will return the index of the first character of the string. it will return -1 if the character is not in the string. it will find the first occurance of the character.
#syntax: string.find(value, start, end) #start and end are optional.

name = name.count('A') # answer:1-- it will return the number of times that the character is in the string.

name = name.split(' ') #it will split the string into a list. it will split the string by the character that we pass to the method. if we don't pass anything, it will split the string by space.
#for example if we have cama in the string, we can split the string by cama:
name = 'Ehsan,Ash,Shayan'
name = name.split(',')

#----------------------------------------------Index------------------------------------

name = 'Ehsan'
name[0] #it will print the first character of the string.
#Index is the position of a character in a string. It starts from 0.
name[-1] #it will print the last character of the string.

#---------------------------------Converting Data---------------------------------------

float(150) #it will convert the number to a float.
int(3.14) #it will convert the number to an integer.
str(99) #it will convert the number to a string.

#----------------------------------------------Input------------------------------------

input('a prompt for the user: ')
#it will print the prompt and wait for the user to enter something. After the user entered the answer, this answer will be replaced by that statement(code).

print('Hello' + ' ' + input('What is your name? '))
#we can use input function inside the print function. it will print the prompt and wait for the user to enter something. After the user entered the answer, this answer will be replaced by that statement(code). Then it will print the rest of the statement(code).

temp = name
name = length
length = temp
print(name,length)
#By using this code, we can swap the content of the boxes.

#----------------------------------------------Hint--------------------------------------

name = input()
#an empty input is a falsy value. here it will give the user a chance to enter the answer again or a cursor.

#-------------------------------Function types------------------------------------------

print() #it is a built-in function. we can use it to print something.
input() #it is a built-in function. we can use it to get input from the user.
len() #it is a built-in function. we can use it to count the number of characters in a string.
type() #it is a built-in function. we can use it to find out the type of the variable.
int() #it is a built-in function. we can use it to convert a number to an integer.
float() #it is a built-in function. we can use it to convert a number to a float.
str() #it is a built-in function. we can use it to convert a number to a string.
help() #it is a built-in function. we can use it to find out how to use a specific method.
round(thing to round , how many decimal points to rount it to) #it is a built-in function. we can use it to round a number.

#-----------------------------------Conditional Statements-------------------------------

#Conditional statements are used to make decisions. we can use if, elif, else to make decisions.
if some condition is true:
    #do something
    #we can call values that are true, truthy and values that are false, falsy.
    #the code inside the if statement is called a code block.
    #There is just true or false not any other values or grey area.
    # Besides 0, None, False, empty string, empty list, empty dictionary, empty set, everything else is true. They are naturally false.(We call them falsy values.)
elif some other condition is true:
    #do something
    #we can have multiple elifs
else:
    #do something
    
car = input('What kind of car do you like?\n')
if car:
    print(f'I like {car} too!')
else:
    print('You did not say anything!')
#We can use if statement to check if the user entered something or not(We are checking the truthiness and exitense of the entered car). If the user entered something, it will print the first statement. If the user did not enter anything(Python concider it as an empty string and by nature it's false.), it will print the second statement.

#***If we want to check if user entered the answer or it's empty:***
if answer:
#or
if answer !='' : #it means that answer is not empty.
    
#***Sometimes we check if answer is empty or not and sometimes we check if answer is true or not.***
#***If we want to check if answer is empty or not:***
if answer:

# if we want to check if answer is true or not:
if answer == True: 
    
print("Correct") if 5>2 else print("Incorrect")
#We can use if else in one line. It's called ternary operator. It's like a SHORT HAND for if else statement.

#not:
a = 200
b = 33
if not b > a:
  print("b is greater than a")
  
#pass statement:
if x < 0:
        pass
#We can use pass statement to avoid getting an error. It means that we don't want to do anything.we can use it if for some reason we want to have an empty code block.
    
#-------------------------------Comparison Operaters------------------------------------

#We can use comparison operators to compare two values.
#We use them anywhere that we want to compare two values. Like inside if or elif statements.
#We can use == to compare two values. for example: 1 == 1, 1 == 2, etc. it means that they are equal.
#we can use != to compare two values. for example: 1 != 1, 1 != 2, etc. it means that they are not equal.
# a > b, a < b, a >= b, a<=b. It means that a is greater than b, a is less than b, a is greater than or equal to b, a is less than or equal to b.

#---------------------------------------Logical Operaters-------------------------------

age>2 and age<8 #it will return True if both of the conditions are true. True and True = True, True and False = False, False and True = False, False and False = False.

age>2 or age<8 #it will return True if one of the conditions is true. True or True = True, True or False = True, False or True = True, False or False = False.

not ((age>2 and age<=8) or age>=65) #it will return True if the condition is false. True = False, False = True. Let's say that age is 22, then the and statement will return false, and  age is not greater than or equal to 65, so the or statement will return false. So the whole statement will return True.
#Logical operators are used to combine conditional statements. We can use not, and, or to combine conditional statements.
#Logical are used to make boolean, logical comparisons or statements.

#-----------------------------------is VS. == -----------------------------------------

a=[1,2,3]
b=[1,2,3]
a==b #it will return True. It means that the values of a and b are equal.
a is b #it will return False. It means that a and b are not the same object. They are two different objects that have the same value. They are two different boxes that have the same content, and their place in the memory is different.
#We can use is to check if two variables are the same object or not. We can use == to check if two variables have the same value or not.

#-----------------------------------randint() -------------------------------------------

#The randint() method returns an integer number selected element from the specified range. The range includes both numbers.
#We can use randint() to generate a random number.
#We have to import random first.
import random
random.randint(start,stop)
#It will return a random number between start and stop. It includes both numbers.
#The randint(a, b) method, specifically, is a function that's associated with the random module object, operating on the internal state of the random number generator contained within the random module. This internal state is the data that the randint method can operate on, consistent with your provided definition of a method.
#****or****
from random import randint
randint(start,stop)
# In this case we don't have to use random. we can use randint() directly.

#--------------------------------For Loops -----------------------------------------
for item in iterable_object:
    #do something with item
    #an iterable object is a collection of items. for example: list, string, etc.
    #item is a place holder variable that we can use in the code block.
    #item changes in every iteration.
    #after it's done the item will go away.
   
for number in range(1, 11):
    print(number)
    #range is a built-in function. it will return a range of numbers.
    #range (stop) like range(7) will return 0 to 6, excluding 7.
    #range(start,stop) like range(1,7) will return 1 to 6, excluding 7.
    #range(start, stop, step) like range(1, 7, 2) will return 1, 3, 5.
    #range(stop, start, step) like range(7, 1, -1) will return 7, 6, 5, 4, 3, 2.
    #range(variable) like range(number).
    
x=0
for i in range(11, 21, 2):
    x += i
    print(x)  
    #it will print the sum of odd numbers from 11 to 20. each time it will add the next odd number to the previous sum and print the new sum till it reaches 20.
    
#for nested loops:
from emoji import emojize
for repeat in range(3):
    for emoji in range(1, 11):
        print(emojize(':grinning_face:'*emoji))
        
#break:
for x in range(1, 11):
    if x == 7:
        break
    print(x)
#It will break the loop when x is equal to 7. It will not print 7.

#continue: with the continue statement we can stop the current iteration of the loop, and continue with the next.
for x in range(1, 11):
    if x == 7:
        continue
    print(x)
#It will skip 7 and continue with the next iteration.

for x in range(1, 11):
    if x == 7:
        continue
    print(x)
else:
    print('Loop finished')
#else will run after the loop is finished.
#if we use break, else will not run.
    
    #-------------------------------Import and use Emojis -------------------------------
    
    #We can use emojis in python. we have to install and import emoji first.
    #to install: pip3 install emoji
    from emoji import emojize
    #then we have to use emojize() function to use emojis.
    print(emojize(':thumbs_up:'))
    #we can find the list of emojis in:
    #https://www.webfx.com/tools/emoji-cheat-sheet/

    #To upgrade:
    #pip install --upgrade emoji
    #"/c/Users/ehsan/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python.exe" -m pip install --upgrade pip
    
    #---------------------------------------Hint----------------------------------------
    
    # if you see that you are repeating a function too many times, you may can use sth else.
    #for example:
 for x in range(1, 21):
    if x == 4 or x == 13:
        print(f'{x} is Unlucky number. :( ')
    elif x % 2 == 0 and x != 4:
        print(f'{x} is Even number. :)')
    else:
        print(f'{x} is Odd number. :)')
        
# Option2

for x in range(1, 21):
    if x == 4 or x == 13:
        state = 'Unlucky'
    elif x % 2 == 0 and x != 4:
        state = 'Even'
    else:
        state = 'Odd'
    print(f'{x} is {state} number. :)')
    
    #-----------------------------------------While Loops ------------------------------
    
    while some condition is true:
    #do something
    #we can use while loop to repeat a code block as long as a condition is true.
    #we can use break to exit the loop.
    #we can use continue to skip the rest of the code block and go to the next iteration.
    #we can use else to run a code block after the loop is finished.
        
    user_response = None
    while user_response != 'please':
        user_response = input('Ah ah ah, you didn\'t say the magic word:\n')
    #we should be careful about infinite loops. we should make sure that the condition will be false at some point.
    #we should make sure that we have a variable that will change in every iteration.
    
    #**** The difference between if, for and while loops:****
    #for loop is used to iterate over a sequence. for example: list, string, etc.
    #while loop is used to repeat a code block as long as a condition is true.
    #if condition is used to check if a condition is true or not just once.
    
    #for example:
    
    for num in range(1, 11):
        print(num)
        #it will print numbers from 1 to 10.
        
    num=1
    while num < 11:
        print(num)
        num += 1
        
#To Break a while or for loop:
while True:
    command = input('Type "exit" to exit: ')
    if (command == 'exit'):
        break
    else:
        print(f'You typed {command}')
    #It will keep asking the user to enter the command. If the user entered exit, it will break the loop and exit the loop. If the user entered sth else, it will print the command and ask the user to enter the command again.
    
for x in range(1,101):
    print(x)
    if x==7:
        break
    
#-----------------------------------------Nice Example------------------------------------------------------

repeat = input('Hey how is it going?\n').lower()
while repeat != 'stop copying me':
    repeat = input(f'{repeat}\n').lower()
print('UGH FINE YOU WIN')

angry = int(input('How many times should I ask you to clean the washroom?\n'))
for angry in range(angry):
    print('Clean the washroom!')
    if angry > 2:
        print("That's it! I'm done")
        break
    
#******check the guessing_game.py file for a nice example.******

#-----------------------------------------List------------------------------------------------------

#List is a collection of items. It is always in square brackets and items are separated by commas.
#List is iterable. we can use the content of the box repeatedly in the code, and Changeable. we can change the content of the box later in the code.
#List can be assigned to other lists.

#List can have different data types. such as: int, float, string, list, etc.
names = ['Ehsan', 'Ash', 'Shayan']
demo_list = ['a', 1, 3.14, True, [1, 2, 3]]

#we can also add variables to a list.
name1 = 'Ehsan'
name2 = 'Ash'
name3 = 'Shayan'
namess = [name1, name2, name3]

#we can use len() to find out the length of a list. like we do for strings.
len(namess)
#The answer will be 3. because we have 3 items in the list.

#if we want to convert any variable to a list, we can use list() function.
#we can use list() to convert a string to a list.
r = range(1, 10)
r_list = list(r)
#or
r_list = list(range(1, 10))

#***Accessing items in a list:***
#we can use index to access items in a list. index starts from [0].
names[0] #it will print the first item in the list.(Ehsan)
#we can also use index as a value of a variable.
best_friend = names[1]
#*****By doing this, we can retrieve a value of a list.*****

#if we wnt to check if a value is in a list or not, we can use in.
'Ehsan' in names #it will return True.
#we can use not in to check if a value is not in a list.
if 'Ehsan' not in names:
    print('Ehsan is not in the list.')
    
#***Iterating over a list:***

nums = [1,2,3,4]
for num in nums:
    print(num)
#It will iterate over the list

letters = ['A','D','F','R']
idx = 0 #stands for index
while idx < len(letters):
    print(letters[idx])
    idx +=1
    
#if we want to use the list just to get sth it's better to use it with for loop like above. but for example in the above situation if we want to print every index with it's related index number we have to use while loop like this:

letters = ['A','D','F','R']
idx = 0 #stands for index
while idx < len(letters):
    print(f'{idx}: {letters[idx]}')
    idx +=1
    
#**********Example**********

names = ['ehsan','arash','amy','sein','belma']
result = ''
for n in names:
    result += n.upper()
#in every loop it will add one of names to result in uppercase

#-----------------------------------------------List Methods--------------------------------------------

#Methods: Methods are like functions, but they're associated with object/classes. Methods in objects are functions that belong to the object.

test = [2,4.5,True,'Ash',11,'a','a','a']
test.append(5) #append is a function which belongs to list as an object. Thus, it's a Method.
#append will add anything that we mention between parentheses, to the end of the list.
#append just gets one argument.

test.extend([7,'i',8])
#extend will solve the problem. by usying extend we can add a list or multiple arguments.

test.insert(2, 'Ehsan')
#The first value is the index number that we want to target and the 2nd one is the value that we want to add.
 
test.clear()
#It will delete all the contents.

test.pop()#It will remove the last item by default
test.pop(1)#The number inside is the index number of the value that we want to be ommited
#the thing is after we deleted a particulare value, by using pop, the computer will keep it for us, so if we want we can return the deleted value and keep it in anouther variable:
test_storage = test.pop(2)
#it will remove the index two value in test and then restore it in test_storage.
   
test.remove(a)
#it will remove the first "a" value that it finds.
#it's useful when we are not sure about the index of an argument that we want to be removed.
#it does not return the value that was removed. 

test.index(2)
#the value inside is the value we are looking for, and the answer will be the index number of that specific value.
test.index('Ash') # index 3
test.index('Ash',1,5)
#value, starting index, ending index****** it will look out for value 'Ash', starting from index one to 5. Answer = 3

test.count('a')
# it will count times that a has been printed which is 3.

test.reverse()
#it will reverse the list and update it.

num = [6,4,5,2,1]
num.sort()
#it will sort the list in ascending order. answer [1,2,4,5,6]
#we can sort string too, it will do it alphabetical, and in case of same names if one of the is in uppercase, priority is with that one.
num.sort(reverse=True)
#it will sort the list in descending order. answer [6,5,4,2,1]
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
#It's a case insensitive sort. It will sort the list in alphabetical order, but it will ignore the case. answer ['banana', 'cherry', 'Kiwi', 'Orange']

#.join(), it's actually a list method which commonly used to concatenate different values of a list, by the rule that we define(like space, dot or a sentence), and *RETURNs* a new string out of that list, which we can use it in a variable.
words = ['He', 'is', 'the', 'best.']
' '.join(words) # 'He is the best.' ---- the object before dot is the rule that we define, and the variable that we want to be joint is in the parentheses. the rule here is spacing. we also can use '. '
sentence = ', '.join(words)
#it concatenate all words and make a sentence as we mentioned by the rule that we defined, and then store it in another variable called sentence

#*******Slicing*******

#it can be used with strings as well.
#for slicing a list from a start to an end point we use square brackets alongside of a list name(like an index), and we seperate them with colons.
#the order is like this: test[start:end:step]
new = test[1,5,2] # answer: new == [4.5, 'Ash', 'a']
new2 = test[1:] # It starts from index one and goes forward till the end with one step each time.
new3 = test[-1:] # it starts from last item to the end(which is none).we can use ane negative number. for example by using -2 it starts for the value prior to the last one.
# ******It's important to understand that it will keep a copy of what we are slicing it doesn't change the original one.
new4 = test[:] # it copies the same list
#if we run new4 == test it's True but if we run new4 is test it's False because it's actually a copy of the original list which is test in this case.

portion = test[:2] # it will start from the 0 index to the number 2 index(third value) by one step. but the ****end index is EXCLUSIVE****like range
portion2 = test[1:3] # start and end
portion3 = test[1:-1]# starts from index number 1 up to exclusive index -1
portion4 = test[::2] # it goes from index 0 up to the last one by 2 steps each time.
portion5 = test[1::2]

numss = [1,2,3,4,5,6]
numss1 = numss[1::-1]# numss1==[2,1] it says start should be index to till the end but with -1 steps
numss2 = numss[:1:-1]# numss2==[6,5,4,3] it says end should be index 1(with end specifications) to start but with -1 steps. so the start will be 6 up to exclusive index1 which is 2
numss3 = numss[2::-1]# numss3==[3,2,1]

#***Reversing string or list by -1 steps:
string = 'Programming is fun!'
string[::-1]

#****Modifying portins of list:

adad = [1,2,3,4,5,6]
adad[1:3] = [a,b,c]
print(adad)# answer is: [1,a,b,c,4,5,6] --- it will replace 2 and 3 with a,b,c because we asked to start from index one up to index 3 which is 4(not included) and replace them with 2nd list

#*****IMPORTANT/ picking a value in an index and reverse it or do sth else:
esmha = ['Ehsan','Amy','EhsanAsh','AmyDil']
esmha2 = esmha[2][::-1]
print(esmha2)# it will pick index 2 from esmha and then because we used slicing by step -1, it will reverse it and the answer is: 'hsAnashA'

'eeehsasaaaaan'[::3]# answer is: ehsan

# ********Swaping*******
names = ['Shiraz','Tehran','Abadan']
names[0], names[2] = names [2], names[0]

#***********************List Comprehension********************#
num = [1,2,3,4,5,6]
num_new = [x*10 for x in num] 
# the simple shape is like this: [___ for ___ in ___]  first parameter is the value that we want to be returned, it can be anything like just a variable all another list with different content, the second one is the place holder variable and the third one is the iterable object that we want to iterate over it, like a list or a string, range, logic statement, etc.
print(num_new)
# it will multiply each number in range 5 by 10 and return a new list of them.
# first value is the value that we want to be returned, and the second one (x) is the place holder variable and the third one is the iterable object that we want to iterate over it.
name = 'Ehsan'
[letter.upper() for letter in name]# ['E', 'H', 'S', 'A', 'N']
# it will return a list of uppercase letters of name.
friends = ['ash','shayan','ehsan','amy']
[friends[0].upper() for friend in friends]# ['Ash', 'Shayan', 'Ehsan', 'Amy']
# it will return a list of uppercase letters of friends.
[num*10 for num in range(1,6)]# [10, 20, 30, 40, 50]

#********Important********
[bool(val) for val in [ 0, '', [] ]] # [False, False, False]

numbers = [1,2,3,4,5,6]
string_list = [str(num) for num in numbers] # ['1', '2', '3', '4', '5', '6']
#or:
string_list = [str(num) + 'Hello' for num in numbers] # ['1Hello', '2Hello', '3Hello', '4Hello', '5Hello', '6Hello']

#********************List Comprehension with Conditional Logic*******************#

numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 ==0] # [2, 4, 6]
odds = [num for num in numbers if num % 2 !=0] # [1, 3, 5]
#or:
ev_od = [num*2 if num % 2 == 0 else num/2 for num in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]
# we can use if else in list comprehension. if the condition is true, it will do the first thing, if it's false, it will do the second thing.
# we can read it like this: for num in numbers, if num % 2 == 0, multiply num by 2, else divide num by 2.
with_vowels = 'This is so much fun!'
' '.join(char for char in with_vowels if char not in 'aeiou') # 'Ths s s mch fn!'
# it will remove all the vowels from the string.

#*********************Nested Lists******************************#

nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]
nested_list[0][1] # 2

for num in nested_list:
    for val in num:
        print(val)
# it will print all the values in the nested list.

#****Nested List Comprehension*****#
[ [print(val) for val in num] for num in nested_list]

[ [num for num in range(1,4)] for val in range(1,4)]
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

[ ['X' if x % 2 != 0 else 'O' for x in range(1,4) ] for val in range(1,4)]
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

#*********************Dictionaries******************************#

#Dictionary is a collection of key value pairs. It is always in curly brackets.

developer = {'name': 'Ehsan', 'age': 30, 'is_developer': True, 77: 'my favorite number'}
#name, age, is_developer are keys and Ehsan, 30, True are values.
#keys are unique. we can not have two keys with the same name.
#keys are immutable. we can not use a list as a key. we can use a tuple as a key.
#values can be anything. they can be mutable or immutable. they can be a list, a dictionary, a tuple, etc.
#like lists, dictionaries are iterable and changeable.
#we can use any data type for values but for keys we mostly use strings and numbers.

# There is another way to create a dictionary:
developer2 = dict(name='Ehsan', age=30, is_developer=True, favorite_number=77)
#we can use dict() to create a dictionary. we can use it to convert a list of tuples to a dictionary.

#if we want to access a value in a dictionary, we can use the key. Like a dictionary, we can use the key to access the value.
developer['name'] # it will return Ehsan.

developer['name'] = 'Arash' # it will change the value of name to Arash.
developer['education'] = 'Master' # it will add education to the dictionary.

#********Looping over a dictionary:********

#for above dictionary:
#in order to loop over a dictionary, we have to use .values() method. it will return the values of the dictionary.
for value in developer.values():
    print(value)
    
for key in developer.keys():
    print(key)
#it will return the keys of the dictionary.

for key, value in developer.items():
    print(f'key is {key} and value is {value}')
#it will return the keys and values of the dictionary.
#dict.items returns a list of tuples. each tuple is a key value pair.
#since we want both key and value, we have to use two variables in the for loop. the name is not important but the order is important. the first variable is the key and the second variable is the value. we can use k,v instead of key, value.

#to test existence of a key in a dictionary:
'name' in developer # it will return True.
44 in developer # it will return False.

#to test existence of a value in a dictionary:
30 in developer.values() # it will return True.
"arash" in developer.values() # it will return False.

#*******Dictionary Methods:*******

empty = developer.clear() # answer is: {}
copy = developer.copy() # it will copy the dictionary and store it in copy.They are equal but they are two different objects.
copy == developer # it will return True.
copy is developer # it will return False.

new = dict.fromkeys(['name', 'age', 'is_developer'], 'unknown') # we can also use None instead of 'unknown' answer is: {'name': 'unknown', 'age': 'unknown', 'is_developer': 'unknown'}
#it will create a dictionary with the keys that we mentioned and the values that we mentioned.
#we can use dict.fromkeys() to create a dictionary with the keys that we mentioned and the values that we mentioned.
#it will be useful when we want to create a dictionary with the same values for all the keys like in a game.
new2 = dict.fromkeys(range(1,10), None)# answer is: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
#we can use range too.

retrieve = developer.get('name') # it will return Ehsan.
#.get() method:
#get() method is used to retrieve a key. it will return None if the key does not exist.
r2 = developer.get('names') # it will return None. it will not give us an error when a key does not exist. ******* it's not like developer['names'] which will give us an error.******
#********Example********
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)
# answer: {'current_score': 0, 'high_score': 0, 'number_of_lives': 0, 'items_in_inventory': 0, 'power_ups': 0, 'ammo': 0, 'enemies_on_screen': 0, 'enemy_kills': 0, 'enemy_kill_streaks': 0, 'minutes_played': 0, 'notifications': 0, 'achievements': 0}
#***********************

#to remove a specific value from a dictionary:

Jeep_info = {'name': 'Jeep Wrangler', 'color': 'Surge Green', 'year': 2022, 'milage': 8756.77, 'Brand new':False}
remove = Jeep_info.pop('milage') # it will remove the value of milage and return it. answer is: 8756.77

Jeep_info.popitem() # it will remove the last item and return it. answer is: ('Brand new', False)

Jeep_info2 = dict(engine='2000 cc')
Jeep_info2.update(Jeep_info) # it will add Jeep_info to Jeep_info2. answer is: {'engine': '2000 cc', 'name': 'Jeep Wrangler', 'color': 'Surge Green', 'year': 2022, 'Brand new': False}

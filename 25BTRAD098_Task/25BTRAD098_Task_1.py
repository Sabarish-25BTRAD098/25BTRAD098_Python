#Task 1
#Question
Print your Name, Department, and College, each on a separate line.
Answer – Python Code
print(&quot;Rahul&quot;)
print(&quot;Computer Science&quot;)
print(&quot;ABC College&quot;)
#Output
Rahul
Computer Science
ABC College

#Task 2
#Question
Print the following pattern.
Answer – Python Code
for i in range(3):
for j in range(7):
print(&quot;*&quot;, end=&quot;&quot;)
print()
#Output
*******
*******
*******

#Task 3
#Question
Print the following using a single print() statement.
Answer – Python Code
print(&quot;Python is Easy&quot;)
#Output
Python is Easy

#Task 4
#Question
Print the number pattern shown in the question.
Answer – Python Code
for i in range(1, 6):
print(str(i) * 1 if i == 1 else &quot;&quot;.join(str(j) for j in range(1, i + 1)))
#Output
1
12
123
1234
12345

#Task 5
#Question
Use \n to print Computer, Science, Engineering on separate lines.
Answer – Python Code
print(&quot;Computer\nScience\nEngineering&quot;)
#Output
Computer
Science
Engineering

#Task 6
#Question
Use \t to print Name, Age, City.
Answer – Python Code
print(&quot;Name\tAge\tCity&quot;)
#Output
Name Age City

#Task 7
#Question
Write a Python program with a single-line comment explaining the purpose of the program.

Answer – Python Code
# Program to calculate and display the area of a rectangle
length = 5
width = 10
print(&quot;Area:&quot;, length * width)
#Output
Area: 50

#Task 8
#Question
Write a Python program using multi-line comments.
Answer – Python Code
&quot;&quot;&quot;
This program demonstrates
the use of a multi-line comment
in Python.
&quot;&quot;&quot;
print(&quot;Python Programming&quot;)
#Output
Python Programming

#Task 9
#Question
Write a program that contains three comments and three print statements.
Answer – Python Code
# Comment 1: Display greeting
print(&quot;Hello!&quot;)
# Comment 2: Display learning message
print(&quot;Learning Python.&quot;)
# Comment 3: Display farewell
print(&quot;Goodbye!&quot;)
#Output
Hello!
Learning Python.
Goodbye!

#Task 10

#Question
Create a variable called name. Store your name and print it.
Answer – Python Code
name = &quot;Rahul&quot;
print(name)
#Output
Rahul

#Task 11
#Question
Store 10, 20, and 30 in three different variables and print them.
Answer – Python Code
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)
#Output
10
20
30

#Task 12
#Question
Convert the string &quot;100&quot; into an integer and display its value and data type.
Answer – Python Code
value = &quot;100&quot;
number = int(value)
print(number)
print(type(number))
#Output
100
&lt;class &#39;int&#39;&gt;

#Task 13
#Question
Convert the integer 25 into a float and display the result and its type.
Answer – Python Code
number = 25
result = float(number)
print(result)
print(type(result))
#Output
25.0
&lt;class &#39;float&#39;&gt;

#Task 14
#Question
Accept the user&#39;s age using input(), convert it to an integer, and display the age.
Answer – Python Code
age = int(input(&quot;Enter your age: &quot;))
print(&quot;Age:&quot;, age)
#Output
Enter your age: 20
Age: 20

#Task 15
#Question
Accept two numbers from the user, convert them to integers, and display their sum.
Answer – Python Code
num1 = int(input(&quot;Enter first number: &quot;))
num2 = int(input(&quot;Enter second number: &quot;))
print(&quot;Sum:&quot;, num1 + num2)
#Output
Enter first number: 10
Enter second number: 20
Sum: 30

#Task 16
#Question
Using an f-string, accept a student&#39;s name, age, and CGPA and display the required sentence.
Answer – Python Code
name = input(&quot;Enter student name: &quot;)
age = int(input(&quot;Enter age: &quot;))
cgpa = float(input(&quot;Enter CGPA: &quot;))
print(f&quot;My name is {name}. I am {age} years old and my CGPA is {cgpa}.&quot;)
#Output
Enter student name: Rahul
Enter age: 20
Enter CGPA: 8.5
My name is Rahul. I am 20 years old and my CGPA is 8.5.

#Task 17
#Question
Accept temperature in Celsius and convert it into Fahrenheit. Display the result using an f-
string with two decimal places.
Answer – Python Code
celsius = float(input(&quot;Enter temperature in Celsius: &quot;))
fahrenheit = (celsius * 9 / 5) + 32
print(f&quot;Temperature in Fahrenheit: {fahrenheit:.2f}&quot;)
#Output
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.00

#Task 18
#Question
Accept an integer and determine whether it is even or odd using the % operator.
Answer – Python Code
number = int(input(&quot;Enter number: &quot;))
if number % 2 == 0:
print(f&quot;{number} is Even&quot;)
else:

print(f&quot;{number} is Odd&quot;)
#Output
Enter number: 25
25 is Odd

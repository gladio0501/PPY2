# -*- coding: utf-8 -*-
"""Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12V1Ndznj0M65EmiKLYNl9VyHnRsJpcJa

Warning:

After each exercise from now on, do a git commit and write in a message what you did.

3.
Write a Python program that takes input from the user to create a list of integers and then performs the following operations:

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers.
  
  c. Sorting: Sort the list in ascending order.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Sorted list: [1, 2, 5, 8, 9]
  ```
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:
numbers_list = input_numbers.split(" ")

# Sorting:
numbers_list.sort()

# Print Output
print("Sorted list:", numbers_list)

"""-----------------------------------------------------------------------------

Difference between Lists and Tuples:

Lists are mutable, meaning their elements can be changed after creation, while tuples are immutable, meaning their elements cannot be changed after creation.
Lists are represented by square brackets [ ], whereas tuples are represented by parentheses ( ).
Lists have methods like append(), insert(), and remove() to modify the list, while tuples do not support such methods due to their immutability.
Lists are typically used when the elements need to be modified or updated frequently, while tuples are used when the data is meant to be constant or unchangeable.

-----------------------------------------------------------------------------

4.
Extend the previous Python program to include tuples. Now, in addition to creating a list of integers from user input, the program should also create a tuple of those integers and perform the following operations:

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers and a tuple of integers.

  c. Sorting: Sort both the list and the tuple in ascending order.

  d. Print Output: Print the sorted list and tuple.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9
  
  Sorted list: [1, 2, 5, 8, 9]
  Sorted tuple: (1, 2, 5, 8, 9)
  ```
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:
numbers_list = input_numbers.split(" ")

# Sorting:
numbers_list.sort()
sorted_tuple = tuple(numbers_list)
# Print Output
print("Sorted list:", numbers_list)
print("Sorted tuple:", sorted_tuple)

"""5.
Extend the previous Python program to demonstrate the manipulation of lists using the append(), insert(), and remove() functions, and to emphasize the immutability of tuples.

  a. Input: Ask the user to enter a series of space-separated integers.

  b. Convert Input: Convert the input string into a list of integers and a tuple of integers.
  
  c. Manipulate List: Use the append(), insert(), and remove() functions to modify the list.
  
  d. Attempt to Modify Tuple: Try to modify the tuple using the same operations as the list.
  
  e. Print Output: Print the modified list and attempt to print the modified tuple.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Modified list: [5, 2, 20, 1, 9, 10]
  Tuple remains unchanged: (5, 2, 8, 1, 9)
  ```
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = input_numbers.split(" ")
numbers_tuple = tuple(numbers_list)
# Manipulate List
#   Append 10 to the list
#   Insert 20 at index 2
#   Remove one elementfrom the list
numbers_list.append(10)
numbers_list.insert(2, 20)
numbers_list.remove(10)
# Attempt to Modify Tuple (this will raise an error)
try:
    #   Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")
try:
    #   Insert 20 at index 2
    numbers_tuple.insert(2, 20)
except AttributeError:
    pass  # Insert operation will also raise an error
try:
    #   Remove one element  from the tuple
    numbers_tuple.remove(10)
except AttributeError:
    pass  # Remove operation will also raise an error

# Print Output
print("Modified list:", numbers_list)
print("Tuple remains unchanged:", numbers_tuple)

"""--------------------------------------------------------------------------------
1. **Set**:
A set in Python is a collection of unique elements that are unordered. This means that you cannot access elements by indices, and the elements are stored in an unordered manner. The main feature of a set is that each element in the set must be unique. Sets are useful when you want to perform set operations, such as mathematical set operations (e.g., union, difference, intersection).

Example of creating a set:
```python
set = {1, 2, 3, 4, 5}  # Creating a set
print(set)  # Displaying the set
```

2. **Dictionary**:
A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are unique in the sense that they allow us to associate specific values with specific keys, making it easy to retrieve values by referring to their corresponding keys. Dictionaries are very useful when you want to store data in the form of key-value pairs, such as dictionary definitions, test scores, survey results, etc.

Example of creating a dictionary:
```python
dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}  # Creating a dictionary
print(dictionary)  # Displaying the dictionary
```
It's important to remember that both in sets and dictionaries, keys (in the case of dictionaries) and elements (in the case of sets) must be hashable, meaning they must be immutable (e.g., numbers, strings, tuples), and they must have a defined hashing method.

--------------------------------------------------------------------------------

6.
Additionally, introduce sets and dictionaries and perform basic operations on them.

  a. ...

  b. ...

  c. ...

  d. ...

  e. Set Operations: Perform union, intersection, and difference operations on the set.

  f. Dictionary Operations: Print the dictionary, add a new key-value pair, and delete an existing key-value pair.

  g. Print Output: Print the modified list, unchanged tuple, set operations results, and updated dictionary.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Original Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  Modified list: [5, 2, 20, 1, 9, 10]
  Tuple remains unchanged: (5, 2, 8, 1, 9)
  Union of set: {1, 2, 5, 9, 10, 11, 12}
  Intersection of set: {8, 5}
  Difference of set: {9}
  Updated Dictionary: {5: 25, 2: 4, 1: 1, 9: 81, 11: 121}

  ```
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = input_numbers.split(" ")
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)
numbers_dict = {"": ""}
for index, element in enumerate(numbers_list):
    numbers_dict[index] = element
# Manipulate List
# Append 10 to the list
# Insert 20 at index 2
# Remove the element 8
numbers_list.append(10)
numbers_list.insert(2, 20)
print(numbers_list)
numbers_list.remove("8")
# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
# Union
# Intersection
# Difference
set_other = {"5", "3", "4", "1"}
set_union = numbers_set.union(set_other)
set_intersection = numbers_set.intersection(set_other)
set_difference = numbers_set.difference(set_other)

# Dictionary Operations
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
# Delete an existing key-value pair
numbers_dict.update(newkey1='portal')
numbers_dict.pop(2)

# Print Output
print("Modified list:", numbers_list)
print("Tuple remains unchanged:", numbers_tuple)
print("Union of set:", set_union)
print("Intersection of set:", set_intersection)
print("Difference of set:", set_difference)
print("Updated Dictionary:", numbers_dict)

"""7. **Built-in Types and Type Conversion**

  Extend the previous Python program to demonstrate the use of built-in types and type conversion. Perform the following operations:

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. Type Conversion: Convert the list to a tuple, set, and dictionary. Convert the tuple to a list, set, and dictionary. Convert the set to a list, tuple, and dictionary. Convert the dictionary to a list, tuple, and set.

  h. Print Output: Print the results of the type conversion operations.

  example:
  ```
  Enter a series of space-separated integers: 5 2 8 1 9

  Tuples are immutable and cannot be modified.
  Original Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  List to Tuple: (5, 2, 20, 1, 9, 10)
  List to Set: {1, 2, 5, 9, 10, 20}
  List to Dictionary: {5: 25, 2: 4, 20: 400, 1: 1, 9: 81, 10: 100}
  Tuple to List: [5, 2, 8, 1, 9]
  Tuple to Set: {1, 2, 5, 8, 9}
  Tuple to Dictionary: {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
  Set to List: [1, 2, 5, 9, 10, 20]
  Set to Tuple: (1, 2, 5, 9, 10, 20)
  Set to Dictionary: {1: 1, 2: 4, 5: 25, 9: 81, 10: 100, 20: 400}
  Dictionary to List: [5, 2, 20, 1, 9, 10, 11]
  Dictionary to Tuple: (5, 2, 20, 1, 9, 10, 11)
  Dictionary to Set: {1, 2, 5, 9, 10, 11, 20}
```
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = list(map(int, input_numbers.split(" ")))
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)
numbers_dict = {"": ""}
for index, element in enumerate(numbers_list):
    numbers_dict[index] = element
numbers_dict.pop(0)
# Manipulate List
# Append 10 to the list
# Insert 20 at index 2
# Remove the element 8
numbers_list.append(10)
numbers_list.insert(2, 20)
print(numbers_list)
numbers_list.remove(8)
# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
# Union
# Intersection
# Difference
set_other = {5, 3, 4, 1}
set_union = numbers_set.union(set_other)
set_intersection = numbers_set.intersection(set_other)
set_difference = numbers_set.difference(set_other)

# Dictionary Operations
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
# Delete an existing key-value pair
numbers_dict.update(newkey1='portal')
numbers_dict.pop(2)

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = dict(enumerate(numbers_list))
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = dict(enumerate(numbers_tuple))
set_to_list = list(numbers_set)
set_to_tuple = tuple(numbers_set)
set_to_dict = dict(enumerate(numbers_set))
dict_to_list = list(numbers_dict.values())
dict_to_tuple = tuple(numbers_dict.values())
dict_to_set = set(numbers_dict.values())

# Print Output
print("List to Tuple:", list_to_tuple)
print("List to Set:", list_to_set)
print("List to Dictionary:", list_to_dict)
print("Tuple to List:", tuple_to_list)
print("Tuple to Set:", tuple_to_set)
print("Tuple to Dictionary:", tuple_to_dict)
print("Set to List:", set_to_list)
print("Set to Tuple:", set_to_tuple)
print("Set to Dictionary:", set_to_dict)
print("Dictionary to List:", dict_to_list)
print("Dictionary to Tuple:", dict_to_tuple)
print("Dictionary to Set:", dict_to_set)

"""8.
Extend the previous Python program to write the output to a file and perform operations on that file.

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. ...

  h. Write Output to File: Write all the results (original inputs, modified data structures, type conversion results) to a file.

  i. Perform Operations on File: Open the file, read its content, and perform some operations like counting the number of lines, finding specific data, etc.

  j. Modify File Content: Modify the content of the file by, for example, changing specific lines or adding new lines.
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = list(map(int, input_numbers.split(" ")))
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)
numbers_dict = {"": ""}
for index, element in enumerate(numbers_list):
    numbers_dict[index] = element
numbers_dict.pop(0)
# Manipulate List
# Append 10 to the list
# Insert 20 at index 2
# Remove the element 8
numbers_list.append(10)
numbers_list.insert(2, 20)
print(numbers_list)
numbers_list.remove(8)
# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
# Union
# Intersection
# Difference
set_other = {5, 3, 4, 1}
set_union = numbers_set.union(set_other)
set_intersection = numbers_set.intersection(set_other)
set_difference = numbers_set.difference(set_other)

# Dictionary Operations
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
# Delete an existing key-value pair
numbers_dict.update(newkey1='portal')
numbers_dict.pop(2)

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = dict(enumerate(numbers_list))
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = dict(enumerate(numbers_tuple))
set_to_list = list(numbers_set)
set_to_tuple = tuple(numbers_set)
set_to_dict = dict(enumerate(numbers_set))
dict_to_list = list(numbers_dict.values())
dict_to_tuple = tuple(numbers_dict.values())
dict_to_set = set(numbers_dict.values())

student_number = input("Enter your student number: ")

# Write Output to File like this:
with open("output.txt", "w") as file:
    file.write("Student Number: " + str(student_number) + "\n")
    file.write("Original List: " + str(numbers_list) + "\n")
    file.write("Original Tuple: " + str(numbers_tuple) + "\n")
    file.write("Original Set: " + str(numbers_set) + "\n")
    file.write("Original Dictionary: " + str(numbers_dict) + "\n")
    file.write("Manipulated List: " + str(numbers_list) + "\n")
    file.write("Manipulated Tuple: " + str(numbers_tuple) + "\n")
    file.write("Union of Set: " + str(set_union) + "\n")
    file.write("Intersection of Set: " + str(set_intersection) + "\n")
    file.write("Difference of Set: " + str(set_difference) + "\n")
    file.write("Updated Dictionary: " + str(numbers_dict) + "\n")
    file.write("List to Tuple: " + str(list_to_tuple) + "\n")
    file.write("List to Set: " + str(list_to_set) + "\n")
    file.write("List to Dictionary: " + str(list_to_dict) + "\n")
    file.write("Tuple to List: " + str(tuple_to_list) + "\n")
    file.write("Tuple to Set: " + str(tuple_to_set) + "\n")
    file.write("Tuple to Dictionary: " + str(tuple_to_dict) + "\n")
    file.write("Set to List: " + str(set_to_list) + "\n")
    file.write("Set to Tuple: " + str(set_to_tuple) + "\n")
    file.write("Set to Dictionary: " + str(set_to_dict) + "\n")
    file.write("Dictionary to List: " + str(dict_to_list) + "\n")
    file.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
    file.write("Dictionary to Set: " + str(dict_to_set) + "\n")

    # print "Content of the file:"
    with open("output.txt", "r") as file:
        print(file.read())

    # Perform Operations on File:
    #   Count the number of lines in the file
    #   Count the number of integers in the file
    #   Add all integers in the file (sum).
    with open("output.txt", "r") as file:
        lines = file.readlines()
    number_of_lines = len(lines)
    number_of_integers = sum([line.count(" ") + 1 for line in lines])
    file.seek(0)
    sum_of_integers = 0
    for line in file:
        words = line.split()
        for word in words:
            if word.isdigit():
                sum_of_integers += int(word)
    print("Number of lines in the file:", number_of_lines)
    print("Number of integers in the file:", number_of_integers)
    print("Sum of integers in the file:", sum_of_integers)

    # Modify the content of the file
    lines[1] = "Student Number: s27668\n" \

               """--------------------------------------------------------------------------------
               **Control Statements:**
               Control statements are used in programming to alter the flow of execution based on certain conditions or criteria. In Python, commonly used control statements include:
               
               `if, elif, else:` These statements are used for conditional execution. They allow the program to execute different blocks of code based on specified conditions.
               
               `for loop:` Used for iterating over a sequence (such as lists, tuples, strings, etc.) or any iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.
               
               `while loop:` Used for executing a block of code repeatedly as long as a specified condition is true. It keeps iterating until the condition becomes false.
               
               
               **Loops:**
               Loops are used for executing a block of code repeatedly. In Python, there are two main types of loops:
               
               `for loop: `As mentioned earlier, the for loop iterates over a sequence or any iterable object.
               
               `while loop:` This loop executes a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.
               
               **Other Statements:**
               This category typically includes other types of statements that don't fall directly under control statements or loops. It can include various types of statements used for different purposes in Python programming, such as:
               
               `Assignment statements:` Assigning values to variables.
               
               `Function calls:` Invoking functions to perform specific tasks.
               
               `Import statements:` Importing modules or packages to use their functionality in the current script or program.
               
               `Exception handling statements: `Statements used for handling exceptions (errors) that may occur during the execution of a program, such as try, except, finally, etc.
               
               `With statements: `Used for resource management, especially for working with files, to ensure that certain resources are properly closed or released after use.
               
               These are fundamental constructs in Python programming that enable you to control the flow of your program, repeat tasks efficiently, and execute various types of statements to achieve desired functionality.
               
               -------------------------------------------------------------------------------
               
               9.  Utilizing the Largest Integer from output.txt
               
                 Task Description:
               
                 Transform the previous task to utilize the largest integer from the output file 'output.txt' instead of asking the user for it.
               
                 1. Read the largest integer from the 'output.txt' file.
                 2. Generate a list of all prime numbers up to the largest integer.
                 3. Print the list of prime numbers.
                 4. Calculate the sum of all prime numbers in the list.
                 5. Determine the largest and smallest prime numbers in the list.
                 6. Check if the largest integer itself is prime and print the result.
                 7. Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'.
                 8. Handle the scenario where the largest integer cannot be found in the file.
               
                 Example:
               
                 If the 'output.txt' file contains:
                 Largest prime number: 20
               
                 The program will generate the list of prime numbers up to 20, perform calculations, and write the results to 'prime_numbers.txt'.
               """ \
            with open("output.txt", "r") as file:
for line in file:
    words = line.split()
    for word in words:
        if word.isdigit():
            number = int(word)
            if largest_number is None or number > largest_number:
                largest_number = number
print(largest_number)
# I really cant understand why I cant read the largest number from the file. I have tried different methods but none of them worked. I will just use 65 instead of it.
largest_number = 65


def primes_sieve2(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False
    primes = []  # Initialize an empty list to store prime numbers

    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)  # Append prime numbers to the list
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False

    return primes


list_of_primes = primes_sieve2(largest_number)
print("List of prime numbers: " + str(list_of_primes) + "\n")
print("Sum of prime numbers: " + str(sum(list_of_primes)) + "\n")
print("Largest prime number: " + str(max(list_of_primes)) + "\n")
print("Smallest prime number: " + str(min(list_of_primes)) + "\n")
if largest_number in list_of_primes:
    print("Largest number is prime")
else:
    print("Largest number is not prime")

with open("prime_numbers.txt", "w") as file:
    file.write("List of prime numbers: " + str(list_of_primes) + "\n")
    file.write("Sum of prime numbers: " + str(sum(list_of_primes)) + "\n")
    file.write("Largest prime number: " + str(max(list_of_primes)) + "\n")
    file.write("Smallest prime number: " + str(min(list_of_primes)) + "\n")
    file.write("Largest number is prime: " + str(largest_number in list_of_primes) + "\n")

    """10.
               In the final main.py file, leave the results from task 8 and 9, commit and push
               """

"""
Exercise 1: Calculate the multiplication and sum of two numbers.
Given two integer numbers, write a Python code to return their product
only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""
def product_sum(num1: str, num2: str):
    if (num1 * num2) <= 1000:
        return num1 * num2
    else:
        return num1 + num2

product_sum =   product_sum(500, 30)  

#print(product_sum)

"""
Exercise 2: Print the Sum of a Current Number and a Previous number
Write a Python code to iterate the first 10 numbers, and in each iteration, 
print the sum of the current and previous number.
"""
previous_num = 0
for i in range(10):
    sum = i + previous_num
    previous_num = i
    #print(sum)
    
"""
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and 
display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
"""
def string_mod():
    word = input("Enter any word")
    for index, char in enumerate(word):
        if index % 2 != 0:
            continue
        print(char)
string_mod()

"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

remove_chars("PYnative", 4) so output must be tive.
Here, you need to remove the first four characters from a string.
remove_chars("PYnative", 2) so output must be native. 
Here, you need to remove the first two characters from a string.
Note: n must be less than the length of the string.
"""
def remove_chars(char, num):
    if num < len(char):
        return char[num:]
    else:
        return f"Enter a number less than length of {char} "
result = remove_chars("PYnative", 100)
print(result)

"""
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.
"""

def list_check(num_list:list):
    if num_list[0] == num_list[-1]:
        return True
    else:
        return False
num_list = [1, 2, 3, 4, 5, 1]
result = list_check(num_list)
print(result)

"""
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.
"""

def list_check(num_list:list):
    assert type(num_list) == list, "num_list should be an array of numbers"
        #raise TypeError("Enter a list of numbers")
    if num_list[0] == num_list[-1]:
        return True
    else:
        return False
num_list = [1, 2, 3, 4, 5, 1]
result = list_check(num_list)
print(result)

"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5
"""

def divisble_by_5(num_list: list):
    if type(num_list) != list:
        raise TypeError("Enter a list a numbers")
    for i in num_list:
        if i % 5 == 0:
            print(i)
num_list = [1, 3, 5, 10, 15, 17, 20]
#num_list = 2
result = divisble_by_5(num_list)
print(result)

"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.
"""
def string_count(string, substring):
    return string.count(substring)
    
result = string_count("I am a very very good boy", "ve")
print(result)

"""
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
def level_num(n):
    for i in range(n + 1):
        for j in range(i):
            print(i, end=' ')
        print('')
result = level_num(5)
print(result)

"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is palindrome. 
A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.
"""


def reverse_num(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

result = reverse_num(1234)
print(result)

"""
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write a Python code to create a new
list such that the latest list should contain odd numbers from the first list
and even numbers from the second list.
"""
def odd_and_even_num(list1: list, list2: list):
    odd_num = [i for i in list1 if i % 2 != 0]
    even_num = [j for j in list2 if j % 2 == 0]
    return odd_num + even_num
    
result = print(odd_and_even_num([10, 20, 25, 30, 35],[40, 45, 60, 75, 90]))
#print(result)

"""
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the 
output shall be “6 3 5 7“, with a space separating the digits.
"""

def reverse_num(num : int):
    rev_num = 0
    while num > 0:
        digit = num % 10
        #rev_num = rev_num * 10 + digit
        num //= 10
        print(digit, end=' ')

result = reverse_num(7536)

"""
Exercise 12: Calculate income tax.
Calculate income tax for the given income by adhering to the rules below;
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

Expected Output:

For example, suppose the income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.
"""


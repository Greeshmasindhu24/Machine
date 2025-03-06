#3.Write a function that returns whether 2 strings are palindrome or not

def is_palindrome(s): return s == s[::-1]
str1, str2 = input("Enter first string: "), input("Enter second string: ")
if is_palindrome(str1) and is_palindrome(str2):
    print("Both strings are palindromes.")
else:
    print("Both strings are not palindromes.")

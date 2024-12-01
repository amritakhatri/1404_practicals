"""
CP1404/CP5632 Practical
Recursion
"""

# Task 1: `do_it(5)` - Predict and debug the recursion

def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# Test the function and observe output
print(do_it(5))  # Expected output: 3


# Task 2: `do_something()` - Print squares of positive numbers in order and reverse

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n >= 0:
        print(n ** 2)
        do_something(n - 1)

# Test the function for normal order (will print squares from n to 0)
do_something(4)  # Expected output: 16, 9, 4, 1, 0


def do_something_reverse(n):
    """Print the squares of positive numbers from n down to 0, on the way back."""
    if n >= 0:
        do_something_reverse(n - 1)  # Recurse first
        print(n ** 2)  # Then print

# Test the function for reverse order (will print squares from 0 to n)
do_something_reverse(4)  # Expected output: 0, 1, 4, 9, 16


# Task 3: Pyramid Program - Calculate the number of blocks in a pyramid with n rows

def pyramid_blocks(n):
    """Calculate the number of blocks in a pyramid with n rows (using a loop)."""
    blocks = 0
    for i in range(1, n + 1):
        blocks += i
    return blocks

# Test the loop-based function
n = 6
print(f"Number of blocks in a pyramid with {n} rows (loop): {pyramid_blocks(n)}")  # Expected output: 21


def pyramid_blocks_recursive(n):
    """Calculate the number of blocks in a pyramid with n rows (using recursion)."""
    if n == 0:
        return 0
    return n + pyramid_blocks_recursive(n - 1)

# Test the recursive function
print(f"Number of blocks in a pyramid with {n} rows (recursive): {pyramid_blocks_recursive(n)}")  # Expected output: 21


# Task 4: Print string from the outside in (recursively)

def print_outside_in(s, i=0):
    """Print a string from the outside in."""
    if i < len(s) // 2:
        print(s[i], s[len(s) - 1 - i], end=" ")
        print_outside_in(s, i + 1)

# Test the function
print_outside_in("Programming")  # Expected output: P g r n o i g m r m a


# Task 5: Palindrome Checker (recursive)

def is_palindrome(s):
    """Check if the string s is a palindrome."""
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")  # Normalize the string
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

# Test the function for palindrome checking
print(is_palindrome("Hannah"))  # Expected output: True
print(is_palindrome("A Toyota's a Toyota"))  # Expected output: True
print(is_palindrome("abcba"))  # Expected output: True
print(is_palindrome("Hello"))  # Expected output: False

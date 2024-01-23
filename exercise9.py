def is_palindrome(number):
    """
    This function checks if a number is a palindrome.

    Args:
      number: The number to be checked.

    Returns:
      True if the number is a palindrome, False otherwise.
    """
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number

# Example usage
number1 = 121
number2 = 125

if is_palindrome(number1):
    print(f"original number {number1}")
    print("Yes. given number is palidrome number")
else:
    print(f"original number {number1}")
    print("No. given number is not palindrome number")

if is_palindrome(number2):
    print(f"original number {number2}")
    print("Yes. given number is palindrome number")
else:
    print(f"original number {number2}")
    print("No. given number is not palindrome number")
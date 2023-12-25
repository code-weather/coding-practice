# '''
# Problem: Find the Largest Number in a List
# You are given a list of integers. Write a Python function to find the largest number in this list.

# Example
# Input: [3, 5, 7, 2, 8, 1]
# Output: 8
# '''

# from typing import List

# def find_largest_number(numbers: List[int]) -> int:
#   if len(numbers) == 0:
#     return None

#   largest_number = numbers[0]
#   for nums in numbers:
#     if nums > largest_number:
#       nums = largest_number

#   return largest_number

# def main():
#   # Test casesg
#   test_cases = [
#     [3, 5, 7, 2, 8, 1],
#     [10, 15, 2, 33, 5],
#     [-3, -1, -7, -2],
#     [1],
#     []
#   ]

#   for case in test_cases:
#     print(f"Input: {case}, Largest Number: {find_largest_number(case)}")

# if __name__ == "__main__":
#   main()

############################################################################################

'''
Problem: Add Digits of a Number
Difficulty Rating: 2/100

Write a Python function that takes a non-negative integer and returns the sum of its digits.

Example:
Input: 123

Output: 6 (because 1 + 2 + 3 = 6)

Input: 0

Output: 0
'''

def sum_of_digits(number: int) -> int:
  # Your code here
  cast_int_to_string = str(number)

  for digit_str in cast_int_to_string:
    

def main():
  # Test cases
  test_cases = [123, 0, 56, 7, 10]

  for number in test_cases:
    result = sum_of_digits(number)
    print(f"Sum of digits in {number} is {result}")

if __name__ == "__main__":
  main()
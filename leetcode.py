from typing import List

def find_largest_number(numbers: List[int]) -> int:
  if len(numbers) == 0:
    return None

  largest_number = numbers[0]
  for nums in numbers:
    if nums > largest_number:
      nums = largest_number

  return largest_number

def main():
  # Test cases
  test_cases = [
    [3, 5, 7, 2, 8, 1],
    [10, 15, 2, 33, 5],
    [-3, -1, -7, -2],
    [1],
    []
  ]

  for case in test_cases:
    print(f"Input: {case}, Largest Number: {find_largest_number(case)}")

if __name__ == "__main__":
  main()

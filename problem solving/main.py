# Here are the Python solutions for the three problems:

### 🔹 Problem 1: Reverse a String
def reverse_string(s: str) -> str:
    return s[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"


### 🔹 Problem 2: Count Vowels in a String
def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s.lower() if char in vowels)

# Example usage
print(count_vowels("Apple"))  # Output: 2


### 🔹 Problem 3: Sum of Digits
def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))

# Example usage
print(sum_of_digits(1234))  # Output: 10

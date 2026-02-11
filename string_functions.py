# 1) Find the length of a string.
s = input("Enter a string: ")
print("Length:", len(s))

# 2) Convert a string to uppercase.
s = input("Enter a string: ")
print("Uppercase:", s.upper())

# 3) Count the number of vowels in a string.
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

# 4) Reverse a string without using slicing.
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

# 5) Check whether a string is palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 6) Count frequency of each character in a string.
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 7) Find how many words are in a sentence.
s = input("Enter a sentence: ")
words = s.split()
print("Word count:", len(words))

# 8) Replace all spaces with hyphens.
s = input("Enter a sentence: ")
print(s.replace(" ", "-"))

# 9) Check whether a string contains only digits.
s = input("Enter a string: ")
print(s.isdigit())

# 10) Remove all special characters from a string.
import string
s = input("Enter a string: ")
clean = ""
for ch in s:
    if ch.isalnum() or ch == " ":
        clean += ch
print("Clean string:", clean)

# 11) Find the first and last occurrence of a character.
s = input("Enter a string: ")
ch = input("Enter character to find: ")
print("First occurrence:", s.find(ch))
print("Last occurrence:", s.rfind(ch))

# 12) Convert a string to title case.
s = input("Enter a string: ")
print("Title case:", s.title())

# 13) Count uppercase and lowercase letters.
s = input("Enter a string: ")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

# 14) Check whether two strings are anagrams.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

# 15) Extract digits from a string.
s = input("Enter a string: ")
digits = ""
for ch in s:
    if ch.isdigit():
        digits += ch
print("Digits:", digits)

# 16) Split a string and join using *.
s = input("Enter a sentence: ")
words = s.split()
print("*".join(words))

# 17) Remove duplicate characters from a string.
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Without duplicates:", result)

# 18) Find the longest word in a sentence.
s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)

# 19) Check whether a string starts and ends with same character.
s = input("Enter a string: ")
if s[0] == s[-1]:
    print("Starts and ends with same character")
else:
    print("Different start and end")

# 20) Sort characters of a string alphabetically.
s = input("Enter a string: ")
sorted_chars = "".join(sorted(s))
print("Sorted string:", sorted_chars)

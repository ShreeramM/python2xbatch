# Anagrams of Strings
"""Input: str1 = “listen”  str2 = “silent”
Output: “Anagram”
Explanation: All characters of “listen” and “silent” are the same.

Input: str1 = “gram”  str2 = “arm”
Output: “Not Anagram”  """

text1 = input("Enter a text: ")
text2 = input("Enter a another text: ")

if sorted(text1.lower()) == sorted((text2.lower())):
    print("Anagram String")
else:
    print("Not a Anagram String")

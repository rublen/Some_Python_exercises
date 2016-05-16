smth = input("Input your text: ").lower()
s = ''
for i in range(0, len(smth)):
    if smth[i].isalpha(): s += smth[i]

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

if (is_palindrome(s)):
    print("Yes, it's palindrom")
else:
    print("No, it's not palindrom")

"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

"""

def recurring(str1):
    for i in range(1,len(str1)):
        if str1[i] == str1[i-1]:
            return  str1[i]
    return None

if __name__ == "__main__":
    print(recurring("acbbac"))
    print(recurring("abcdef"))

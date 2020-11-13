"""
Daily Coding Problem: Problem #604 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Grammarly.
Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.
Soundex maps every name to a string consisting of one letter and three numbers, like M460.
One version of the algorithm is as follows:
1.	Remove consecutive consonants with the same sound (for example, change ck -> c).
2.	Keep the first letter. The remaining steps only apply to the rest of the string.
3.	Remove all vowels, including y, w, and h.
4.	Replace all consonants with the following digits:
o	b, f, p, v → 1
o	c, g, j, k, q, s, x, z → 2
o	d, t → 3
o	l → 4
o	m, n → 5
o	r → 6
5.	If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, Jackson and Jaxen both map to J250.
Implement Soundex.
Daily Coding Problem: Problem #349 [Hard] 
"""
# code from https://rosettacode.org/wiki/Soundex#Python
def soundex2(codes,word):
   dictionary =dict( (char,i+1) for i,code in enumerate(codes) for char in code )
   convert = lambda char:dictionary.get(char) # if char not in dict returns None
   sdx = ''.join(str(convert(char)) for char in word.lower()[1:] if convert(char) )
   sdx = word[0].upper()+''.join(dict.fromkeys(sdx))
   return sdx[0:4].ljust(4,'0')


if __name__ == "__main__":
   codes = ("bfpv","cgjkqsxz", "dt", "l", "mn", "r")
   print(soundex2(codes,"Jackson"))
"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Implement a URL shortener with the following methods:
•	shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
•	restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""
import random

ShortUrls = dict()

def shorten(url):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortUrl = ''
    #there are 44,261,653,680 possible pairs
    if len(ShortUrls) >= 44261653680:
        return None
    while True:
        shortUrl = ''.join(random.choices(map, k=6))
        if shortUrl not in ShortUrls:
            ShortUrls[shortUrl] = url
            return shortUrl

def restore(short):
    if short in ShortUrls:
            return ShortUrls[short]
    else:
        return None


if __name__ == '__main__':
    short = shorten('www.google.com')
    print(short)
    print(restore(short))



#### Daily Coding Problem: Problem #172 [Medium] 
```
This problem was asked by Dropbox.
Given a string s and a list of words words, where each word is the same length, find all starting indices
of substrings in s that is a concatenation of every word in words exactly once.
For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], 
since "dogcat" starts at index 0 and "catdog" starts at index 13.
Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since
there are no substrings composed of "dog" and "cat" in s.
The order of the indices does not matter.

```

#### Daily Coding Problem: Problem #173 [Easy] 
```
This problem was asked by Stripe.
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
```

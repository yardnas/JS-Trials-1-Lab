"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given list"""

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return an array of all even numbers"""

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    """Given a list, return all elements at odd numbered indices"""

    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result


def print_as_numbered_list(items):
    """Given a list, output a numbered list"""

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    """Return a list of numbers in a certain range"""

    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced withh '*'"""

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case"""
    pass

    # camel_case = []

    # for word in string.split('_'):
    #     camel_case.append(word[0.upper()])


def longest_word_length(words):
    """Return the length of the longest word in the given list of words"""

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    """Truncate repeating characters into one character"""
    result = []

    for char in string:
        # compare current to previous (-1)
        if (len(result) == 0) or (char != result[len(result)-1]):
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced"""

    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

        if parens < 0:
            return false
    
    return parens == 0
    

def compress(string):
    """Return a compressed version of the given string"""

    pass
    

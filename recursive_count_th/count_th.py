'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #  this if statement will check if the length of the given word is more than two characters. If it is less than three characters
    #  Then this will return 0
    if len(word) < 2:
        return 0
    #  we used the recursive method with an if statement. The if statement checks if the word has "th" and the we call the function with
    # in the function.
    return (1 if word[:2] == "th" else 0) + count_th(word[1:])
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    if "th" in word:
        newword = word.replace("th", '*USEDTOBEATHHERE*', 1) #  had to add the replacement string instead of '' because it would cause t and h's surrounding other th's to collapse and be counted
        return count_th(newword) + 1
    else:
        return 0


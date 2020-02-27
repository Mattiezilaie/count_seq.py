# Author: Mahtab Zilaie
# Date: February 24 2020
# Description: Generator function that generates a sequence and goes indefinitely


def count_seq():
    """generator function with no parameters starts with '2' """
    num = '2'
    while True:
        yield int(num)
        num = count_seq_helper(num)


def count_seq_helper(num):
    """helper function"""
    index = 0    # set index to 0
    count = 1    # set count to 1
    ret = ""     # set ret to str
    while index < len(num):    # index is less than length of num
        if index >= (len(num) - 1) or num[index] != num[index + 1]:   # i >= 2nd-last i in num or num i !=i to the right
            ret += str(count)        # ret adds count as str
            ret += num[index]       # added to ret is value at number's index
            count = 1               # count set to 1 again
        else:
            count += 1            # one added to count
        index += 1               # one added to index
    return ret



#for num in count_seq():
#   print(num)

#g = count_seq()
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

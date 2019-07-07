def sum_array(array):
    '''Return sum of all items in array'''
    array_sum = 0
    for x in array:
        array_sum = array_sum + x
    return array_sum

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    #'''Return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    '''Return word in reverse'''
    reverse_word = ""
    for x in word:
        reverse_word = x + reverse_word
    return reverse_word

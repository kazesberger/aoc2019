from functools import reduce

# 6 digits
# x = range(240298, 784956)
# reduce(append if !=, digits).length == 5
# reduce(append if <=, digits).length == 6

# 556789
candidates = range(240298, 784956)

def isDigitsNeverDecreaseAndContainsEqual(x, y):
    # print(f'{x,y}')
    if (not x[0]):
        return (False,False,-1)
    yDigit = int(y)
    if int(x[-1]) < yDigit:
        return (x[0] and True,x[1], yDigit)
    if int(x[-1]) == yDigit:
        return (x[0], True, yDigit)
    return (False,False,-1)

isValidNumber = lambda x : x[1][0] and x[1][1]

meh = lambda x : x[0] and x[1]

def foo(num):
    return (num, reduce(isDigitsNeverDecreaseAndContainsEqual,str(num),(True,False,0)))

# len(list(filter(isValidNumber, [reduce(isDigitsNeverDecreaseAndEqualOnce,str(number),(True,1,0)) for number in candidates])))
len(list(filter(isValidNumber, [foo(number) for number in candidates])))

reduce(isDigitsNeverDecreaseAndContainsEqual,str(111111),(True,False,0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(223450),(True,False,0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(123789),(True,False,0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(784889),(True,False,0))

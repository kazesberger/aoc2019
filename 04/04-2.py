from functools import reduce

# 6 digits
# x = range(240298, 784956)
# reduce(append if !=, digits).length == 5
# reduce(append if <=, digits).length == 6

# 556789
candidates = range(240298, 784956)

def isDigitsNeverDecreaseAndContainsEqual(x, y):
    print(f'{x,y}')
    if (not x[0]):
        return (False,False, False,-1)
    yDigit = int(y)
    if int(x[-1]) < yDigit:
        return (x[0],x[1], False, yDigit)
    if int(x[-1]) == yDigit:
        return (x[0], True if not x[2] else False, True, yDigit)
    return (False,False, False,-1)

isValidNumber = lambda x : x[1][0] and x[1][1]

meh = lambda x : x[0] and x[1]

def foo(num):
    return (num, reduce(isDigitsNeverDecreaseAndContainsEqual,str(num),(True,False, False,0)))

# len(list(filter(isValidNumber, [reduce(isDigitsNeverDecreaseAndEqualOnce,str(number),(True,1,0)) for number in candidates])))
len(list(filter(isValidNumber, [foo(number) for number in candidates])))

reduce(isDigitsNeverDecreaseAndContainsEqual,str(112233),(True,False,False, 0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(123444),(True,False,False, 0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(111122),(True,False,False, 0))
reduce(isDigitsNeverDecreaseAndContainsEqual,str(784889),(True,False,False, 0))


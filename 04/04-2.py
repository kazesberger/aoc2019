from functools import reduce

# 6 digits
# x = range(240298, 784956)
# reduce(append if !=, digits).length == 5
# reduce(append if <=, digits).length == 6

# 556789
candidates = range(240298, 784956)

# def isDigitsNeverDecreaseAndContainsEqual(x, y):
#     # print(f'{x,y}')
#     if (not x[0]):
#         return (False,False, False,-1)
#     yDigit = int(y)
#     if int(x[-1]) < yDigit:
#         return (x[0],x[1], False, yDigit)
#     if int(x[-1]) == yDigit:
#         return (x[0], True if not x[2] else False, True, yDigit)
#     return (False,False, False,-1)

def isDigitsNeverDecrease(acc,y):
    # print(f'isDigitsNeverDecrease {acc,y}')
    if not acc[0]:
        return (False, -1)
    yDigit = int(y)
    if int(acc[-1]) <= yDigit:
        return (acc[0], yDigit)
    return(False, -1)

def getFrequencies(s):
    all_freq = {}

    for c in s:
        if c in all_freq:
            all_freq[c] += 1
        else:
            all_freq[c] = 1
    return all_freq

def hasPairAndNoBigGroup(numStr):
    f = getFrequencies(numStr).values()
    return 2 in f and max(f) == 2

def hasPair(numStr):
    f = getFrequencies(numStr).values()
    return 2 in f

def validateRules(numStr):
    # print(numStr)
    return (numStr, reduce(isDigitsNeverDecrease, numStr, (True,0))[0], hasPair(numStr))

isValidNumber = lambda x : x[1] and x[2]
len(list(filter(isValidNumber, [validateRules(str(number)) for number in candidates])))

# [validateRules(str(number)) for number in candidates]

for number in candidates:
    print(number)
    print(validateRules(str(number)))

validateRules(str(112233))
validateRules(str(123444))
validateRules(str(111122))

# reduce(isDigitsNeverDecrease,str(112233),(True,0))[0] and hasPairAndNoBigGroup(112233)
# reduce(isDigitsNeverDecreaseAndContainsEqual,str(123444),(True,False,False, 0))
# reduce(isDigitsNeverDecreaseAndContainsEqual,str(111122),(True,False,False, 0))
# reduce(isDigitsNeverDecreaseAndContainsEqual,str(784889),(True,False,False, 0))

# [x] neverDecrease -> simple once false always false
# [ ] hasAtLeast1Pair ->

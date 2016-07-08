def fibs(num):
    result = [0,1]
    for i in xrange(num-2):
        result.append(result[-1]+result[-2])
    return result
print fibs(10)
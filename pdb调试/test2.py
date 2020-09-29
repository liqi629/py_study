import pdb

def getAverage(a,b):
    result = a+b
    print ("result=%d"%result)
    return result
a = 100
pdb.set_trace()
b = 200
c = a+b
ret = getAverage(a,b)
print (ret)

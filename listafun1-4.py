def testaDivisor(a,b):
    if(a%b==0):
        return True
    elif(a%b==b):
        return True
    else:
        return False
print(testaDivisor(3,1))
print (testaDivisor(6,18))
print(testaDivisor(18,6))
print (testaDivisor(14,4))

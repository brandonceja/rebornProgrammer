# Given an array of integers and a key, determine if the sum of any two integers equals the key.

integers = [0,2,1,1,0,2,10,3]
key = 4

arrayLength = len(integers)

for i1 in range(arrayLength-1):
    for i2 in range(arrayLength-1-i1):
        if (integers[i1]+integers[i2+1+i1]) == key:
            print(str(integers[i1]) + " POS[" + str(i1) + "] plus " + 
                str(integers[i2+1+i1]) + " POS[" + str(i2+1+i1) +
                "] equals the key [" + str(key) +"]")
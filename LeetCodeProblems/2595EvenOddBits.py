num = 50 

bnV = bin(num)[2:]

evenCount = 0
oddCount = 0

bnV = bnV[:-1]

for i,j in enumerate(bnV):
    if j == "1":
        if i % 2 == 0:
            evenCount+=1
        else:
            oddCount+=1


print([evenCount,oddCount])
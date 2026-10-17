n = 4421

result  = 0
sum = 0 
productDigit = 1
while n > 0 :
    lastDigit = n % 10
    productDigit *= lastDigit
    sum += lastDigit
    n = n // 10 

result = productDigit - sum 
print(result)
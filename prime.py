n =int(input("Enter a number: "))

count = 0
for i in range(1,n+1):
    
    if n%i == 0:
        count+=1
    else:
        continue
    
if count == 2:
    print("Yes it is a prime number")
else:
    print("It is not a prime number")
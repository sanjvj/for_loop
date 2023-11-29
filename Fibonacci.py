n = int(input("Enter total no of terms: "))
a = int(input("Enter starting number:"))
b = int(input("Enter second number: "))
print(a)
print(b)
for i in range(0,n-2):
   c = a+b
   temp =b 
   b = c
   a = temp
   print(c)
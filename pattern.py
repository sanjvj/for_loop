#Hollow Pattern

for i in range(0,5):
    for j in range(0,5):
        if i==0 or i ==4 or j==0 or j==4:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

print() #Leaving space 


#Left Traingle
for i in range(0,5):
    for j in range(0,5):
        if i>=j:
            print("*", end=' ')
    print() 
    

print() #Leaving space 


#Inverted triangle
for i in range(0,5):
    for j in range(0,5):
        if i<=j:
            print("*", end=' ')
    print() 
    

print() #Leaving space 
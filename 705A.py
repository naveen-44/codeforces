n = int(input())
s = ""
for i in range(n):
    if(i==0):
        s = "I hate "
    elif(i%2==1):
        s += "that I love "
    else:
        s += "that I hate "
 
s+= "it"
print(s)

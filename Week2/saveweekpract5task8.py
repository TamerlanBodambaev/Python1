S = str(input("Input text: "))
count=0
i=0
count2=0
s=" "
for i in range(len(S)):
    if S[i]==' ' :
        count+=1
    if S[i]=='.' :
        count+=1
    i+=1
    
     
print("The number of words  is: " + str(count))

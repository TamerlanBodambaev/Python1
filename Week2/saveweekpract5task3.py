import re
S = str(input("Input text: "))
count=0
i=0
s=" "
for i in range(len(S)):
    if S[i]=='.' :
        count+=1
           
    i+=1
S=S.replace(".","")     
print("The number of replaced  is: " + str(count))
print("The new text is: "+ S)

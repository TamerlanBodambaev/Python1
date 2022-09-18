import re
S = str(input("Input text: "))
count=0
i=0
count2=0
s=" "
for i in range(len(S)):
    if S[i]=='a' :
        count+=1
           
    i+=1
    count2+=1
S=S.replace("a","o")     
print("The number of replaced  is: " + str(count))
print("The new text is: "+ S)
print("The number of character is: " + str(count2))

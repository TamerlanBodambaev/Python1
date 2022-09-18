S = str(input("Input text: "))
count=0
i=0
b=0
for i in range(len(S)):
    if S[i]=="t":
        count+=1
print("The nubmer 't' in the text is: " + str(count))    

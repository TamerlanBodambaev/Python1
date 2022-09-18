S = str(input("Input text: "))
count=0
i=0

for i in range(len(S)):
    if S[i]=="(":
      while S[i]!=")":
          print(S[i])
          i+=1
    i+=1      
print(")")

S = str(input("Input text: "))
find = str(input("Input the word what you wanna count: "))
count=0
i=0
count2=0
s=' '
b=0
find=find.split(" ")
word = S.split(" ")
for b in range(len(word)):
    if word[b]==find[0]:
        count+=1
    b+=1        
print("The number of words  is: " + str(count))

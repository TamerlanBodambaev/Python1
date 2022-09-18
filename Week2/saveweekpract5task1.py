S = str(input("Input the russian text: "))
count=0
i=0
for i in range(len(S)):
    if S[i]=='е' :
        count+=1
        if S[i-1]!=" "  :
            count-=1
            
    i+=1
print('Количество слов начинающийся на "е": ' + str(count))

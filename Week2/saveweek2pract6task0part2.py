n=int (input ('Введите длину массива:'))
a=[]
for i in range (n):
    print ('Введите',i,'элемент:')
    a.append (int (input () ) )
print ('Исходный массив: ',a)
for i in range (n):
    if a[i]<0:
        a[i]=-a[i]
print ('Полученный массив: ',a)

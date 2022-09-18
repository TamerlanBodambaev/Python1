n=int (input ('Введите длину массива\n'))
m=int (input ("Введите число M\n"))
x=[]
y=[]
for i in range (n):
    print ("Введите ", i, "элемент:")
    x. append (int (input () ) )
for i in range (n):
              if abs (x[i] ) >m:
                    y.append(x[i])
print ('Введённое число M:',m)
print ('Мaссив X:', x)
print ('Массив Y:',y)

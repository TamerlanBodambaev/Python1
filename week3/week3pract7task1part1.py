s=input("Input the shape and number:")
cmd, para=s.split(":")
print(cmd,"->",para)

if cmd=='cir':
    r = float(para)
    print(f"arear={r*r*3.14}")
elif cmd=='rect':
    sw, sh = (float(x) for x in para.split())
    print(f"area={sw*sh}")
elif cmd=='trapz':
    ul, bl, h = (float(x) for x in para.split())
    print(f"area={(ul+bl)*h/2}")
else:
    print("wrong input")

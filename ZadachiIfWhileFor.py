from random import *
from keyboard import *

while True:
    
    print("Hello!")
    if is_pressed("esc"): break
    







from random import *
M=randint(100,1000)
print("Poes on ",M,"m")
while M>0:
    m=int(input("Mitu meetri tahad osta?"))
    if M>=m:
        M-=m
        print("Meil on jäänud ",M,"m")
    else:
        print("Tahad rohkem kui meil on")
        v=input("Kas tahad jääk osta?")
        if v=="jah":
            print("Kang on teie oma")
            M=0
        else:
            print("Ei taha, siis ei taha!")
print("Pood on tühi!",M)









Km=s_pikkus=10 #3 задача
print("1. päeval pikkus oli ",Km)
print("Terve tee pikkus oli",round(s_pikkus,2))
for p in range(2,8):
    km*=1.1
    print(p,". päeval pikkus oli ",round(km,2))
    s_pikkus+=Km
    print(p,"terve tee pikkus oli", round(s_pikkus,2))



















Ask_P=Ask_N="" #1 задача
while type(Ask_P)!=int:
    try:
        Ask_P=int(input("Mitu numbreid?"))
    except ValueError:
        print("Ainult täisarvud!")

if Ask_P>0:
    try:
        Ask_N=int(input("Number"))
    except ValueError:
        print("Ainult täisarvud")
    Ask_P-=1
    maks=Ask_N
while Ask_P>0:
    try:
        Ask_N=int(input("Number"))
    except ValueError:
        print("Ainult täisarvud!")
    Ask_P-=1
    if Ask_N>maks: maks=Ask_N
    print(maks)
else:
    print("Ei saa leida max")
r=5
h=10
f=10
t=int(input("enter the time in minuts"))
Vtank= 3.14*r**2*h
Vwater= f*t
if Vwater>Vtank:
    print("over flow condition")
    print("volume of",Vwater-Vtank)
elif Vwater==Vtank:
    print("tank full")
else:
    print("underflow condition")
    ht=Vwater/(3.14*r**2)
    hr=h-ht
    print(f"filled hight{ht}\nRemaining hight {hr}")

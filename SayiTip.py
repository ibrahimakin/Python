n=input("sayi")
liste=list(n)
listea=list(n)
liste.sort()
if liste==listea:
    print("Artan")
else:
    liste.reverse()
    if liste==listea:
        print("Azalan")
    else:
        print("Dalgalı")
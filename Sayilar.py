print("{ ( [ <   SAYILAR   > ] ) }")
n=input("Sayı: ")
while int(n)>0:
    a=1
    t=0
    d=0
    for i in n:
        print(a,".Basamak",i)
        t=t+int(i)
        a=a+1
    print("Basamak Toplamı:",t)
    n=int(n)
    liste=[1,1]
    i=1
    while(i<n):
        liste.append(liste[i]+liste[i-1])
        i=i+1
    print(n,". Fibonacci Sayisi: ",liste[n-1])
    if n==2 or n==3 or n==5 or n==7:
        d=1
        print("Asaldır.")
    elif n==1 or n%2==0:
            d=2
            print("Asal Değil.")
    for k in range(3,int((n)**(1/2)+1),2):
        if d==2:
            break
        if n%k==0:
            print("Asal değil.")
            d=3
            break
    if d!=1 and d!=2 and d!=3:
        print("Asaldır.")
    if n>=10:
        liste=list(str(n))
        listea=list(str(n))
        liste.sort()
        if liste==listea:
            print("Artan Sayı")
        else:
            liste.reverse()
            if liste==listea:
                print("Azalan Sayı")
            else:
                print("Dalgalı Sayı")
    n=input("Sayı: ")
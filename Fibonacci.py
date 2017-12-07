n=int(input("Sayi: "))
while(n>0):
    liste=[1,1]
    i=1
    while(i<n):
        liste.append(liste[i]+liste[i-1])
        i=i+1
    print(n,". Fibonacci Sayisi: ",liste[n-1])
    n=int(input("Sayi: "))
import random
#Dört sayı kaldığında takılabilir.
liste=[1,2,3,4,5,6,7,8,9,10]
print(liste)
while len(liste)>0:
    h=int(input("Hamle: "))
    if liste.count(h)!=0 and liste.count(h+1)!=0:
        liste.remove(h)
        liste.remove(h+1)
        r=0
    print(liste)
    n=random.randint(1,10)
    while liste.count(n)==0 or liste.count(n+1)==0:
        n=random.randint(1,10)
        if len(liste)==0:
            break
    if liste.count(n)!=0 and liste.count(n+1)!=0:
        print("Hamlem: ",n,",",(n+1))
        liste.remove(n)
        liste.remove(n+1)
        r=1
    print(liste)
    if (liste.count(1)==0 or liste.count(2)==0) and (liste.count(2)==0 or liste.count(3)==0) and (liste.count(3)==0 or liste.count(4)==0) and (liste.count(4)==0 or liste.count(5)==0) and (liste.count(5)==0 or liste.count(6)==0) and (liste.count(6)==0 or liste.count(7)==0) and (liste.count(7)==0 or liste.count(8)==0) and (liste.count(8)==0 or liste.count(9)==0) and (liste.count(9)==0 or liste.count(10)==0):
        break
if r==1:
    print("Ben Kazandım.")
else:
    print("Sen Kazandın.")
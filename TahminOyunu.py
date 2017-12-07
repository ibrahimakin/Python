import random
print("Bitirmek için 0'a basın.")
print("1 . Oyun")
n=int(input("Tahminin Nedir?(1 ve 10 arası): "))
o=0
k=0
while(n>0):
    if n!=1 and n!=2 and n!=3 and n!=4 and n!=5 and n!=6 and n!=7 and n!=8 and n!=9 and n!=10:
        print("1 ve 10 Arasında ! ! !")
        break
    h=random.randint(1,10)
    if n==h:
        while(n==h):
            n=random.randint(1,10)
        print("Önerim: ",n)
        print(h,"veya",n," Seçimini Yap!")
    else:
        print("Önerim: ",h)
        print(n,"veya",h," Seçimini Yap!")
    tercih=int(input("Tercihin Nedir?: "))
    if tercih!=n and tercih!=h:
        print("Bilemedin",n,"veya",h,"olacaktı.")
        break
    if tercih==h:
        print("Bildin")
        k=k+1
    else:
        print("Bilemedin")
    o=o+1
    print((o+1),". Oyun")
    n=int(input("Tahminin Nedir?(1 ve 10 arası): "))
print(o,"oyunda",k,"kez kazandın.")
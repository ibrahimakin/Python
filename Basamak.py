n=input("Sayı: ")
a=1
t=0
for i in n:
    print(a,".Basamak",i)
    t=t+int(i)
    a=a+1
print("Basamak Toplamı:",t)
# 2. Soru
print("2. Soru")
toplam='0'
for i in range(5):
    toplam+=str(i*i)
print(toplam)
# 3. Soru
def deger(n):
    i=n*n
    basamak=[]
    for b in str(i):
        basamak.append(b)
    toplam=int(basamak[0])+int(basamak[-1])
    return(toplam)
print("3.Soru Deneme:")
a=int(input("Sayı"))
print(deger(a))
sonuc=0
print("3. Soru:")
for a in range(12,1002):
    sonuc+=deger(a)
print(sonuc)
# 4. Soru
print("4. Soru")
cumle=list(input("Bir Şey Yazın."))
for i in cumle:
    if cumle.count(i)>1:
        cumle.remove(i)
print(cumle)
print(len(cumle))
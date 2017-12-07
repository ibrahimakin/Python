#4 milyona kadar çift fib toplamı(TMM)
a,b,toplam,c=1,1,0,3
while b<4000000:
    a,b=b,a+b
    print(c,". Fibonacci Sayısı: ",b)
    c+=1
    if (b)%2==0:
        toplam+=b
print("Toplam: ",toplam)
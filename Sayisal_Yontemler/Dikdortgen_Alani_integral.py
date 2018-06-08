def f(x):
    return(x**2+2)
n=1024
a,b=1,3
integral=0
integral2=0
integral3=0
h=(b-a)/n
for i in range(n):
    integral+=f(a+i*h)*h
#print(integral)
for i in range(1,n+1):      #dikdortgenler ustte kalsaydi.
    integral2+=f(a+i*h)*h
for i in range(1,2*n,2):    #dikdortgenlerin yarisi ustte kaldiysa.
    integral3+=f(a+(i*h)/2)*h
print("",integral,"\n",integral2,"\n",integral3)
# 3 Basamakli 2 carpanla max. palindromik
palindromik=[]
for i in range(100,1000):
    for j in range(100,1000):
        if str(i*j)==str(i*j)[::-1]:
            palindromik.append(i*j)
print(max(palindromik))
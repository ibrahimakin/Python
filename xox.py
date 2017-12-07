from random import randint
print('  🎮_.-X-O-X-._🎮')
mat=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print(mat[0])
print(mat[1])
print(mat[2])
k=2
while mat[0].count(' ')>0 or mat[1].count(' ')>0 or mat[2].count(' ')>0:
    x,y=int(input(" Koordinat [X]❓: ")),int(input(" Koordinat [Y]❓: "))
    x,y=y,x
    x=x-1
    y=y-1
    while mat[x][y]=='X' or mat[x][y]=='O':
        print("Başka Hamle Deneyin.😃")
        x,y=int(input(" Koordinat [X]❓: ")),int(input(" Koordinat [Y]❓: "))
        x,y=y,x
        x=x-1
        y=y-1
    mat[x][y]='X'
    print(mat[0])
    print(mat[1])
    print(mat[2])
    if (mat[0]==['X','X','X']) or (mat[1]==['X','X','X']) or (mat[2]==['X','X','X']):
        k=1
        break
    elif mat[0][0]=='X' and mat[1][0]=='X' and mat[2][0]=='X':
        k=1
        break
    elif mat[0][1]=='X' and mat[1][1]=='X' and mat[2][1]=='X':
        k=1
        break
    elif mat[0][2]=='X' and mat[1][2]=='X' and mat[2][2]=='X':
        k=1
        break
    elif mat[0][0]=='X' and mat[1][1]=='X' and mat[2][2]=='X':
        k=1
        break
    elif mat[2][0]=='X' and mat[1][1]=='X' and mat[0][2]=='X':
        k=1
        break
    k=2
    o,u=randint(0,2),randint(0,2)
    while mat[o][u]!=' ':
        o,u=randint(0,2),randint(0,2)
        if mat[0].count(' ')==0 and mat[1].count(' ')==0 and mat[2].count(' ')==0:
            k=3
            break
    if k==3:
        break
    print("  Hamlem (O)😎: ",(u+1),",",(o+1))
    mat[o][u]='O'
    print(mat[0])
    print(mat[1])
    print(mat[2])
    if (mat[0]==['O','O','O']) or (mat[1]==['O','O','O']) or (mat[2]==['O','O','O']):
        k=0
        break
    elif mat[0][0]=='O' and mat[1][1]=='O' and mat[2][2]=='O':
        k=0
        break
    elif mat[0][0]=='O' and mat[1][0]=='O' and mat[2][0]=='O':
        k=0
        break
    elif mat[0][1]=='O' and mat[1][1]=='O' and mat[2][1]=='O':
        k=0
        break
    elif mat[0][2]=='O' and mat[1][2]=='O' and mat[2][2]=='O':
        k=0
        break
    elif mat[2][0]=='O' and mat[1][1]=='O' and mat[0][2]=='O':
        k=0
        break
if k==1:
    print("  Sen Kazandın.😕")
elif k==0:
    print("  Ben Kazandım.😏")
else:
    print("  Berabere.😐")
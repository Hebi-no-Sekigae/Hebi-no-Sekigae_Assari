import random as ran #"random"を呼び出し、"ran"と省略できるようにする

print(" へびの席替え あっさり v1.2")
print()

number = int(input("人数を入力 ＞")) #席替えをする人数を聞く

hai = [] #配列「hai」を作る。

for a in range(number): #配列「hai」に出席番号を代入
    if a+1 < 10:
        hai.append("0"+str(a+1))
    else:
        hai.append(str(a+1))

yoko = int(input("横の席数を入力 ＞")) #横の席数を聞く

ran.shuffle(hai) #配列「hai」をシャッフル。

print()

d=0
for c in hai:
    d+=1
    if d==yoko:
        print(c,end="\n")
        d=0
    else:
        print(c,end=" ")
print(end="\n")
print()

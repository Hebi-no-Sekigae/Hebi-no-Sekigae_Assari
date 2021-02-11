import random as ran #"random"を呼び出し、"ran"と省略できるようにする
import math

print(" へびの席替え あっさり v1.1.2")
print()

number = int(input("人数を入力 ＞")) #席替えをする人数を聞く

hai = [] #配列「hai」を作る。

for a in range(number): #配列「hai」に出席番号を代入
    b=a+1
    if b < 10:
        hai.append("0"+str(b))
    else:
        hai.append(str(b))

yoko = int(input("横の席数を入力 ＞")) #横の席数を聞く
tate = math.ceil(number / yoko) #縦の席数を計算する。

ran.shuffle(hai) #配列「hai」をシャッフル。

print()

d=0
for c in range(number):
    d+=1
    if d==yoko:
        print(hai[c],end="\n")
        d=0
    else:
        print(hai[c],end=" ")
print(end="\n")
print()

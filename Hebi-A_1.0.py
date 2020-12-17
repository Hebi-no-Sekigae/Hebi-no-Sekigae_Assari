import random as ran #"random"を呼び出し、"ran"と省略できるようにする

print(" へびの席替え あっさり Ver 1.0")
print()

number = int(input("人数を入力 ＞")) #席替えをする人数を聞く

hai = [] #配列「hai」を作る。　

for a in range(number+1): #配列「hai」に出席番号を代入
    if a != 0:
        if a < 10:
            hai.append("0"+str(a))
        else:
            hai.append(str(a))

yoko = int(input("横の席数を入力 ＞")) #横の席数を聞く
tate = int(number / yoko) #縦の席数を計算する。後ろの列が半端な場合は1少なく代入
amari = number % yoko #一番うしろの席が半端かどうかを調べる

ran.shuffle(hai) #配列「hai」をシャッフル。 

print()
y = yoko
for b in range(tate): #結果を表示
    print(hai[y-yoko:y])
    y += yoko

if amari != 0: #一番うしろの席（半端な場合）の結果を表示
    print(hai[number-amari:number])
    amari = 0

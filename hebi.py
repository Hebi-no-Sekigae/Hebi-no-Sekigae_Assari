import random as ran#"random"を呼び出し、"ran"と省略できるようにする

print(" へびの席替え あっさり v1.2")
print()

number = int(input("人数を入力 ＞"))#席替えをする人数を聞く
yoko = int(input("横の席数を入力 ＞"))#横の席数を聞く
mae0 = input("前列優先者の出席番号を入力＞")#前列希望者の出席番号を聞く
print()

if mae0 != "":
    mae0=mae0.split(",")

#mae0(文字列)からmae1(数)に変換
mae1=[]
for a in mae0:
    mae1.append(int(a))
    
usi = []#前列ではない人
al = []#全員(まとめる)

#usiに前列ではない人代入
maetf = False
for a in range(number):
    for b in mae1:
        if b == a+1:
            maetf = True
    if maetf==False:
        usi.append(a+1)
    maetf = False
    
ran.shuffle(usi)#前列ではない人混ぜ混ぜ
ran.shuffle(mae1)#前列の人混ぜ混ぜ

maeama = len(mae1)%yoko#前列の人の余りの人数

if maeama == 0:#前列の人余らない場合
    al = mae1 + usi
else:#前列の人余る場合
    maemae = mae1[:-maeama]
    maeusi = mae1[-maeama:]
    usimae = usi[:yoko-maeama]
    usiusi = usi[yoko-maeama:]
    naka = maeusi + usimae
    ran.shuffle(naka)
    al = maemae + naka + usiusi

alal=[]
for a in al:
    if a < 10:
        alal.append("0"+str(a))
    else:
        alal.append(str(a))

b=0
for a in alal:
    b+=1
    if b==yoko:
        print(a,end="\n")
        b=0
    else:
        print(a,end=" ")

print(end="\n")
if b != 0:
    print(end="\n")
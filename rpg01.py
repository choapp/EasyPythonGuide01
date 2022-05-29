# coding: utf-8
hp = 100
while True:
    in1 = input("モンスターがあらわれた！コマンド？(1:たたかう 2:ぼうぎょ 3:にげる):")
    if in1 == "1":
        print("モンスターを攻撃した！")
        hp = hp - 10
        if hp <= 0:
                print("モンスターを倒した！")
                break
    elif in1 == "2":
        print("モンスターから身を守った！")
    elif in1 == "3":
        print("モンスターから逃げ出した！")
        break
    else:
        print("コマンドが違います")
print("プログラム終了")
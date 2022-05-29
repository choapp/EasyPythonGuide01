# coding: utf-8
import random

hp1 = 100 # 自分のHP
hp2 = 100 # モンスターのHP
while True:
    # 自分の攻撃ターン
    in1 = input("モンスターがあらわれた！コマンド？(1:たたかう 2:ぼうぎょ 3:にげる):")
    if in1 == "1":
        hp2 = hp2 - 10
        print("モンスターを攻撃した！10ポイントのダメージを与えた！")
        print(hp2)
        if hp2 <= 0:
                print("モンスターを倒した！")
                break
    elif in1 == "2":
        print("モンスターから身を守った！")
    elif in1 == "3":
        print("モンスターから逃げ出した！")
        break
    else:
        print("コマンドが違います")
    # モンスターの攻撃ターン
    in2 = str(random.randint(1, 2)) # モンスターのコマンドを乱数で決定する。モンスターは逃げないので1-2を設定
    # print(in2) # 確認用

    if in2 == "1":
        hp1 = hp1 - 10
        print("モンスターに攻撃された！10ポイントのダメージを受けた！")
        print(hp1)
        if hp1 <= 0:
                print("モンスターに敗れた！")
                break
    elif in2 == "2":
        print("モンスターは身を守った！")

print("プログラム終了")
# coding: utf-8
# モンスターリスト
import random

# データ格納スペース
monster = []

# モンスター作成関数
def create():
    # データの作成
    m1 = { "name" : "スライム", "HP" : 20, "ATK" : 10, "DFC" : 10 }
    m2 = { "name" : "ゴブリン", "HP" : 30, "ATK" : 15, "DFC" : 10 }
    m3 = { "name" : "トロール", "HP" : 50, "ATK" : 40, "DFC" : 5 }

    # データの登録
    monster.append(m1)
    monster.append(m2)
    monster.append(m3)

# モンスター取り出し関数
def load():
    idx = random.randint(0, len(monster)-1)
    return monster[idx]

# モンスターデータの作成
create()

# モンスターデータの読み込み
mon = load()

# 確認
print(mon)
# coding: utf-8
# モンスターリスト

# データ格納スペース
monster = []

# データの作成
m1 = { "name" : "スライム", "HP" : 20, "ATK" : 10, "DFC" : 10 }
m2 = { "name" : "ゴブリン", "HP" : 30, "ATK" : 15, "DFC" : 10 }
m3 = { "name" : "トロール", "HP" : 50, "ATK" : 40, "DFC" : 5 }

# データの登録
monster.append(m1)
monster.append(m2)
monster.append(m3)

# 確認
print(monster)
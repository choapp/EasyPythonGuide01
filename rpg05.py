# coding: utf-8
# =============
# モンスターRPG
# (C)Choapp.
# 2022.
# =============

#機能拡張
import time # スリープ
import random # 乱数

# タイトルに関する処理
## タイトルの表示
def title():
    print("")
    print("【モンスターと戦う簡単なRPGゲーム】")
    while True:
        cd = input("あなたの名前(入力したらエンターキー):")
        if cd == "":
            print("＊エラー：何か入力してね")
        elif cd == " ":
            print("＊エラー：何か入力してね")
        else:
            return cd # 戻り値でユーザー名を返す

# モンスターに関する処理
## データ格納スペース
monsters = []

## モンスター作成関数
def create():
    # データの作成
    m1 = { "NAME" : "スライム", "HP" : 30, "ATK" : 10, "DFC" : 18 }
    m2 = { "NAME" : "ゴブリン", "HP" : 50, "ATK" : 15, "DFC" : 15 }
    m3 = { "NAME" : "スケルトン", "HP" : 70, "ATK" : 30, "DFC" : 30 }
    m4 = { "NAME" : "トロール", "HP" : 80, "ATK" : 45, "DFC" : 5 }
    m5 = { "NAME" : "ナイト", "HP" : 100, "ATK" : 40, "DFC" : 40 }
    m6 = { "NAME" : "ドラゴン", "HP" : 150, "ATK" : 50, "DFC" : 50 }

    # データの登録
    monsters.append(m1)
    monsters.append(m2)
    monsters.append(m3)
    monsters.append(m4)
    monsters.append(m5)
    monsters.append(m6)


## モンスター取り出し関数
def loadmonster():
    idx = random.randint(0, len(monsters)-1) # モンスターをランダムに取り出し
    return monsters[idx] # 戻り値でモンスターデーターを返す

## モンスターデータの作成
create()

# ユーザーに関する処理
user = { "NAME" : "戦士", "HP" : 100, "ATK" : 20, "DFC" : 20 }

# 基本処理
## バトル処理
def battle(user, monster):
    # name:ユーザーの名前 mname:モンスターの名前
    name = user["NAME"]
    mname = monster["NAME"]

    # hp1:自分のHP hp2:モンスターのHP
    hp1 = user["HP"]
    hp2 = monster["HP"]

    # atk1:自分の攻撃力 atk2:モンスターの攻撃力
    atk1 = user["ATK"]
    atk2 = monster["ATK"]

    # dfc1:自分の防御力 dfc2:モンスターの防御力
    dfc1 = user["DFC"]
    dfc2 = monster["DFC"]

    # 防御フラグ
    grd1 = 1
    grd2 = 1

    # カウント
    cnt = 0 # ターン数
    global win,esc

    while True:
        # カウントアップ
        cnt = cnt + 1
        # ステータス表示
        print("●第" + str(cnt)+"ターン")
        print("名前:「" + name + "」 HP:" + str(hp1) + "/" + str(user["HP"]))
        print("攻撃力:" + str(atk1) + " 防御力:" + str(dfc1))
        print("「" + mname + "」との戦い")

        # 自分の攻撃ターン
        in1 = input("コマンド？(1:たたかう 2:ぼうぎょ 3:にげる):")
        if in1 == "1":
            # ダメージの計算
            atk = atk1-(dfc2*grd2) # ユーザーの攻撃力-(モンスターの防御力*モンスターの身の守り)
            if atk < 1:
                atk = 1
            dmg = random.randint(0, atk) # ダメージ計算

            #ダメージ処理
            if dmg > 0:
                hp2 = hp2 - dmg
                print("「" + mname + "」を攻撃した！" + str(dmg) + "ポイントのダメージを与えた！")
                if hp2 <= 0:
                        print("「" + mname + "」を倒した！")
                        print("「" + name + "」はレベルが上がった！")

                        # カウントアップ
                        win = win + 1 # 勝利数+1

                        # レベルアップ
                        levelup()

                        # 1秒待つ
                        print("・・・")
                        time.sleep(1)

                        break
                elif hp2 > monster["HP"]/2:
                    print("「" + mname + "」はまだ元気そうだ")
                else:
                    print("「" + mname + "」は弱っている")
            else:
                print("攻撃は外れた")
        elif in1 == "2":
            print("「" + name + "」は身の守りを固めた！")
            grd1 = 1
        elif in1 == "3":
            print("「" + mname + "」から逃げ出した！")
            
            # 1秒待つ
            print("・・・")
            time.sleep(1)

            if random.randint(0, 3)%3 == 0:
                print("「" + mname + "」からうまく逃げられた！")

                # カウントアップ
                esc = esc + 1 # 逃げた数+1

                break
            else:
                print("しかし逃げられなかった")
                grd1 = 0 # 防御力0
        else: # コマンドにない入力
            print("コマンドが違います")
            grd1 = 0 # 防御力0

        # 1秒待つ
        print("・・・")
        time.sleep(1)

        # モンスター防御フラグの解除
        grd2 = 1

        # モンスターの攻撃ターン
        in2 = str(random.randint(1, 2)) # モンスターのコマンドを乱数で決定する。モンスターは逃げないので1-2を設定
        # print(in2) # 確認用

        if in2 == "1":
            # ダメージの計算
            atk = atk2-(dfc1 * grd1) # モンスターの攻撃力-(ユーザーの防御力 * ユーザーの身の守り)
            if atk < 1:
                atk = 1
            dmg = random.randint(0, atk) # ダメージ計算

            #ダメージ処理
            if dmg > 0:
                hp1 = hp1 - dmg
                print("「" + mname + "」に攻撃された！" + str(dmg) + "ポイントのダメージを受けた！")
                print(hp1)
                if hp1 <= 0:
                        print("「" + mname + "」に敗れた！")
                        
                        gameover()
                        break
            else:
                print("攻撃をかわした！")
        elif in2 == "2":
            print("「" + mname + "」は身の守りを固めた！")
            grd2 = 2

        # ユーザー防御フラグの解除
        grd1 = 1

## ステータスアップ
def levelup():
    user["HP"] = user["HP"] + random.randint(1, 5)
    user["ATK"] = user["ATK"] + random.randint(1, 5)
    user["DFC"] = user["DFC"] + random.randint(1, 5)

## ゲームオーバー
def gameover():
    ## 1秒待つ
    print("・・・")
    time.sleep(1)

    ## メッセージ表示
    print("【ゲームオーバー】")
    print("残念ながら「" +user["NAME"]+"」は倒れた。またの挑戦を待っているぞ！")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("プレイヤー名:「" +user["NAME"]+"」")
    print("対戦回数:" + str(cnt) + "回")
    print("勝利回数:" + str(win) + "回")
    print("逃げた数:" + str(esc) + "回")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("お疲れ様でした！")
    print("(C)Choapp.")

    #終了
    exit()

# タイトルの呼び出し
user["NAME"] = title() # ユーザー名を受け取る

# ようこその表示
print("ようこそ「" + user["NAME"] + "」")

# 説明
print("あなたはある世界に迷い込んだ。何故かモンスターが次々に現れ、戦わなければならない。とりあえずがんばれ！")

# カウント
cnt = 0 # 対戦回数
win = 0 # 勝利回数
esc = 0 # 逃げた回数

# モンスターとの戦闘
while True:
    # モンスターデータの読み込み
    monster = loadmonster()

    # カウントアップ
    cnt = cnt + 1

    # 1秒待つ
    print("・・・")
    time.sleep(1)

    # メッセージ
    print("というわけで" + monster["NAME"] + "があらわれた！")

    # 戦闘関数呼び出し
    battle(user, monster)
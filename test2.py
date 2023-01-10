### インポート
import sys
import random

### 行動パターン
act_dic = {"a":"攻撃", "b":"防御", "c":"魔法"}

### ダメージマトリックス
arr = ([[3,3],[3,1],[2,4]],     # プレイヤー攻撃
       [[1,3],[0,0],[3,0]],     # プレイヤー防御
       [[4,2],[0,3],[1,1]])     # プレイヤー魔法

### HP初期値
play_hp = 20
mons_hp = 20

### 素早さ
play_agi = 8
mons_agi = 7

### 関数定義
def battle(arg):

    ### ダメージマトリックスの配列
    if arg == "プレイヤー":
        f_idx = 1
    else:
        f_idx = 0

    if   play_act == "攻撃" and mons_act == "攻撃":
        f_damage = arr[0][0][f_idx]
    elif play_act == "攻撃" and mons_act == "防御":
        f_damage = arr[0][1][f_idx]
    elif play_act == "攻撃" and mons_act == "魔法":
        f_damage = arr[0][2][f_idx]
    elif play_act == "防御" and mons_act == "攻撃":
        f_damage = arr[1][0][f_idx]
    elif play_act == "防御" and mons_act == "防御":
        f_damage = arr[1][1][f_idx]
    elif play_act == "防御" and mons_act == "魔法":
        f_damage = arr[1][2][f_idx]
    elif play_act == "魔法" and mons_act == "攻撃":
        f_damage = arr[2][0][f_idx]
    elif play_act == "魔法" and mons_act == "防御":
        f_damage = arr[2][1][f_idx]
    elif play_act == "魔法" and mons_act == "魔法":
        f_damage = arr[2][2][f_idx]

    ### ダメージを返す
    return f_damage

### 戦闘が終了するまでループ
while True:

    ### 行動入力
    print(">>> 行動を選択してください")
    print(">>> a:攻撃 b:防御 c:魔法 q:終了")
    player = input(">>> ")

    ### 終了
    if player == "q":
        break

    ### 入力エラー
    elif player not in list(act_dic.keys()):
        print("＋＋ a:攻撃 b:防御 c:魔法 q:終了 を入力してください")
        print()
        continue

    ### 行動保存
    play_act = act_dic[player]
    mons_act = act_dic[random.choice(list(act_dic.keys()))]

    ### 戦闘順決定
    play_agi2 = play_agi * (1 + random.randrange(100) / 100)
    mons_agi2 = mons_agi * (1 + random.randrange(100) / 100)
    char_dic = {"プレイヤー":play_agi2, "モンスター":mons_agi2}

    ### 行動順設定
    for character in sorted(char_dic.items(), key=lambda arg: arg[1], reverse=True):

        ### 行動判定
        damage = battle(character[0])

        ### 行動結果を表示
        if character[0] == "プレイヤー":
            mons_hp -= damage
            mons_hp = max(0, mons_hp)
            print("＋＋ プレイヤーは{}を実行！ モンスターは{}のダメージ".format(play_act, damage))
        else:
            play_hp -= damage
            play_hp = max(0, play_hp)
            print("＋＋ モンスターは{}を実行！ プレイヤーは{}のダメージ".format(mons_act, damage))

        ### HP判定
        if   mons_hp == 0:
            print()
            print("＋＋ モンスターを倒しました！ ＋＋")
            sys.exit()
        elif play_hp == 0:
            print()
            print("＋＋ プレイヤーは倒されました... ＋＋")
            sys.exit()

    ### 空行
    print()
# -*- coding: utf-8 -*-
# 移動関数
def move(n, start, via, end):
    if n > 1:
        move(n-1, start, end, via)

    desc = "{0}番を{1}軸から{2}軸へ移動".format(n, start, end)
    print(desc)

    if n > 1:
        move(n-1, via, start, end)

# メイン
i = input("円盤の枚数を入力しなさい：")
su = int(i)

# 呼び出し
move(su, "木下", "中谷", "齋藤")



# -*- coding: utf-8 -*-
# 移動関数
def move(n, start, via, end):
    global cnt
    if n > 1:
        move(n-1, start, end, via)

    desc = "{3}回目：{0}番を{1}から{2}へ移動".format(n, start, end, cnt)
    print(desc)
    cnt=cnt+1

    if n > 1:
        move(n-1, via, start, end)

# メイン
i = input("円盤の枚数を入力しなさい：")
su = int(i)
cnt = 1
# 呼び出し
move(su, "木下", "中谷", "齋藤")



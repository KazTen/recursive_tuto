# -*- coding: utf-8 -*-
from turtle import *

def recur (length, depth=0):
    if depth <= 0 :
        forward(length)
    else :
        recur(length / 3, depth - 1)
        left(60)
        recur(length / 3, depth - 1)
        left(-120)
        recur(length / 3, depth -1)
        left(60)
        recur(length / 3, depth - 1)


# メイン
i = input("長さの初期値を入力：")
length = int(i)
i = input("深さの値を入力：")
d = int(i)

penup()  # ペンを上げる
setposition(-400, -200)  # 描き始めの位置を設定
pendown()  # ペンを下げる
recur (length, d)

done()  # これがないと描画画面が閉じる




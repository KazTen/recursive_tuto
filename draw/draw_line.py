# -*- coding: utf-8 -*-
from turtle import *

def recur (length, depth=0, ang=60):
    if depth <= 0 :
        forward(length)
    else :
        recur(length / 3, depth - 1, ang)
        left(ang)
        recur(length / 3, depth - 1, ang)
        left(ang * (-2))
        recur(length / 3, depth -1, ang)
        left(ang)
        recur(length / 3, depth - 1, ang)

def recur2 (length, depth=0, ang=90):
    if depth <= 0 :
        forward(length)
    else :
        recur2(length / 3, depth - 1, ang)
        left(ang)
        recur2(length / 3, depth - 1, ang)
        left(-ang)
        recur2(length / 3, depth -1, ang)
        left(-ang)
        recur2(length / 3, depth - 1, ang)
        left(ang)
        recur2(length / 3, depth - 1, ang)

# メイン
i = input("長さの初期値を入力：")
length = int(i)
i = input("曲げる角度を入力（30以上90未満）")
angle = int(i)
i = input("深さの値を入力：")
d = int(i)

screensize(1024, 768)
penup()  # ペンを上げる
setposition(-500, -200)  # 描き始めの位置を設定
pendown()  # ペンを下げる
if angle <= 60:
    recur(length, d, angle)
else:
    recur2(length, d, angle)

done()  # これがないと描画画面が閉じる




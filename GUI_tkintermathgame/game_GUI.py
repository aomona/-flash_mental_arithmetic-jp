import tkinter as tk
from tkinter import messagebox as mbox
import random
from re import S
from time import sleep
print ("難易度を選択してください")
print ("1を選ぶと簡単,2を選ぶと普通,3を選ぶと難しいになります")
difficulty = input("1~3の数字を入力してください:")
if int(difficulty) == 1:
    digits = 9
elif int(difficulty) == 2:
    digits = 99
elif int(difficulty) == 3:
    digits = 999
else:
    print ("難易度の取得に失敗しました、正しい数値を入力してもう一度お試しください")
    print ("このゲームはまもなく自動で閉じます")
    sleep(3)
if int(difficulty) == 1 or int(difficulty) == 2 or int(difficulty) == 3:
    print ("3")
    sleep(1)
    print ("2")
    sleep(1)
    print ("1")
    sleep(1)
    print ("スタート!!!")
    for i in range(5):
        value = [random.randint(1,digits),random.randint(1,digits)]
        answer = value[0] + value[1]
        p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
        if answer == int(p_answer):
            print ("正解！")
        else:
            print ("不正解!残念!")
    else:
        print ("お疲れ様でした！")
        print ("このゲームはまもなく自動で閉じます")
        sleep(3)


# 画面を作成
window = tk.Tk()
# 画面サイズ
window.geometry("400x200")
# 画面タイトル
window.title("デスクトップアプリ")

# 文章を表示
label = tk.Label(window, text=text)
label.pack()

# テキストボックスを作成
text_box = tk.Entry(window)
text_box.pack()

# OKボタン
def ok_button():
    # テキストボックスの内容を取得
    s = text_box.get()
    # ダイアログを表示
    mbox.showinfo("結果", s + "と入力されました")
# OKボタンを表示
okbutton = tk.Button(window, text="OK", command=ok_button)
okbutton.pack()

# 画面を表示
window.mainloop()

import random
<<<<<<< HEAD
from re import S
from time import sleep
print ("難易度を選択してください")
print ("1を選ぶと簡単,2を選ぶと普通,3を選ぶと難しいになります")
=======
from time import sleep
print ("難易度を選択してください")
print ("1を選ぶと簡単,2を選ぶと普通,3を選ぶと難しいの難易度になります")
>>>>>>> b0b8c6f51b11065285efca89f0f2d3e725b75def
difficulty = input("1~3の数字を入力してください:")
if int(difficulty) == 1:
    digits = 9
    print ("難易度が「簡単」に設定されました")
elif int(difficulty) == 2:
    digits = 99
    print ("難易度が「普通」に設定されました")
elif int(difficulty) == 3:
    digits = 999
    print ("難易度が「難しい」に設定されました")
else:
    print ("難易度の取得に失敗しました、正しい数値を入力してもう一度お試しください")
<<<<<<< HEAD
    print ("このゲームはまもなく自動で閉じます")
    sleep(3)
if int(difficulty) == 1 or int(difficulty) == 2 or int(difficulty) == 3:
=======
    print ("このゲームはまもなく終了します")
    sleep(3)
if int(difficulty) == 1 or int(difficulty) == 2 or int(difficulty) == 3:
    print ("問題数を入力してください(おすすめ:5~10)")
    number_of_times = input("希望の問題数を記入してください:")
>>>>>>> b0b8c6f51b11065285efca89f0f2d3e725b75def
    print ("3")
    sleep(1)
    print ("2")
    sleep(1)
    print ("1")
    sleep(1)
<<<<<<< HEAD
    print ("スタート!!!")
    for i in range(5):
=======
    print ("スタート！！")
    for i in range(int(number_of_times) - 1):
        value = [random.randint(1,digits),random.randint(1,digits)]
        answer = value[0] + value[1]
        p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
        if answer == int(p_answer):
            print ("正解！")
            print ("次へ")
        else:
            print ("不正解!もう一回!")
            p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
            if answer == int(p_answer):
                print ("正解！")
                print ("次へ!")
            else:
                print ("不正解!")
                print ("次へ！")
    else:
>>>>>>> b0b8c6f51b11065285efca89f0f2d3e725b75def
        value = [random.randint(1,digits),random.randint(1,digits)]
        answer = value[0] + value[1]
        p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
        if answer == int(p_answer):
            print ("正解！")
        else:
            print ("不正解!もう一回!")
            p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
            if answer == int(p_answer):
                print ("正解！")
            else:
                print ("不正解!")
        print ("お疲れ様でした！")
<<<<<<< HEAD
        print ("このゲームはまもなく自動で閉じます")
        sleep(3)
=======
        print ("このゲームはまもなく終了します")
        sleep(3)
        
>>>>>>> b0b8c6f51b11065285efca89f0f2d3e725b75def

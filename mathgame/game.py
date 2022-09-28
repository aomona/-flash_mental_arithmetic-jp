import random
from re import S
print ("難易度を選択してください")
print ("1を選ぶと1ケタ,2を選ぶと1~2ケタ,3を選ぶと1~3ケタ")
difficulty = input("1~3の数字を入力してください:")
if int(difficulty) == 1:
    digits = 9
elif int(difficulty) == 2:
    digits = 99
elif int(difficulty) == 3:
    digits = 999
else:
    print ("難易度の取得に失敗しました、正しい数値を入力してもう一度お試しください")
if int(difficulty) == 1 or int(difficulty) == 2 or int(difficulty) == 3:
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


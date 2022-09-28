import random
from re import S
value = [random.randint(1,10),random.randint(1,10)]
answer = value[0] + value[1]
p_answer = input(str(value[0]) + "+" + str(value[1]) + "=")
if answer == int(p_answer):
    print ("正解！")
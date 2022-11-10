R='不正解!'
Q='不正解!もう一回!'
P='このゲームはまもなく終了します'
N='正解！'
M='='
L='+'
J=input
F=str
C=int
A=print
from ast import Import
import sys,random as K
from time import sleep as H
A('難易度を選択してください')
A('1を選ぶと簡単,2を選ぶと普通,3を選ぶと難しいの難易度になります')
G=J('1~3の数字を入力してください:')
if C(G)==1:D=9;A('難易度が「簡単」に設定されました')
elif C(G)==2:D=99;A('難易度が「普通」に設定されました')
elif C(G)==3:D=999;A('難易度が「難しい」に設定されました')
else:A('難易度の取得に失敗しました、正しい数値を入力してもう一度お試しください');A(P);H(3)
if C(G)==1 or C(G)==2 or C(G)==3:
	A('問題数を入力してください(おすすめ:5~10)');O=J('希望の問題数を記入してください:');A('3');H(1);A('2');H(1);A('1');H(1);A('スタート！！')
	for S in range(C(O)-1):
		B=[K.randint(-1*D,D),K.randint(1,D)];I=B[0]+B[1];E=J(F(B[0])+L+F(B[1])+M)
		if I==C(E):A(N);A('次へ')
		else:
			A(Q);E=J(F(B[0])+L+F(B[1])+M)
			if I==C(E):A(N);A('次へ!')
			else:A(R);A('次へ！')
	else:
		B=[K.randint(-1*D,D),K.randint(1,D)];I=B[0]+B[1];E=J(F(B[0])+L+F(B[1])+M)
		if I==C(E):A(N)
		else:
			A(Q);E=J(F(B[0])+L+F(B[1])+M)
			if I==C(E):A(N)
			else:A(R)
		A('お疲れ様でした！');A(P);H(3)
        
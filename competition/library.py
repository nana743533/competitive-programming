# 1 
from itertools import combinations, product

lia = list(combinations([1,2,3], 2))    #! ～から２つ取り出した場合の一番大きいものを選べ
print(lia)                              #! タプルのリストを返す

N=3
lib = product([1,0], repeat=N)                    #! 直積(複数の集合から新しい集合を作る)
print(list(lib))                                  #! ビット全探索に使う

# 2
from collections import deque, defaultdict
lic = [0,1,2,3,4,5]
q = deque(lic)                                    #! 幅優先探索に使う
print(q)

while q:
    l = q.popleft()
    r = q.pop()
    print(l,r,q)

d = defaultdict(int)                 #! キーがうざいときに辞書の代わりに使う, 特にループするときとか
print(d["unknown"])                  #! 最初にデフォルト値を入れとくと、知らないキーでも出してくれる。（intは0）
d["unknown"] += 1
d["unknown"] = 5
print(d["unknown"])

# 3
from heapq import heapify, heappop, heappush                 #! 優先度付きキューを作る
#! 要素の中で最小のものを高速に取り出す, 最小値に要素を入れるのも高速, 最大値の時にも使える
q = [3,1,5,4,0,2]
heapify(q)
print(q)
while q: 
    x = heappop(q)
    print(x, q)
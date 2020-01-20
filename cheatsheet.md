# PythonCheatSheet

## 01 出力

- 区切り文字の指定

区切り文字指定なし

```python
print(1,2,3)
```

```python
1 2 3
```

改行を指定

```python
print(1,2,3,sep='\n')
```

```python
1
2
3
```

---

区切り文字なし

```python
print(a,b,c,sep='')
```

```python
123
```

- 末尾文字の指定

```python
print("a",end="")
print("b")
```

```python
ab
```

通常は `\n` が末尾文字になっているため改行する

- リストの出力

1 次元リストの出力

```python
Lists=[1,2,3,4,5]
print(List)
```

```python
[1, 2, 3, 4, 5]
```

1 次元リストをアンパックして出力

```python
Lists=[1,2,3,4,5]
print(*List)
```

```python
1 2 3 4 5
```

2 次元リストの各行を出力する

```python
Lists=[[1,2,3],[4,5,6]]
for List in Lists:
    print(List)
```

```python
[1, 2, 3]
[4, 5, 6]
```

2 次元リストの各要素を出力する

```python
List=[[1,2,3],[4,5,6]]
for Row in List:
    for Col in Row:
        print(Col)

```

```python
1
2
3
4
5
6
```

## 02 入力

### 1 行 / 1 列

- **整数を変数に格納する**

```python
2
```

```python
N=int(input())
print(N)
```

```python
2
```

- **文字列を 1 つの変数に格納する**

```python
Hello world!
```

```python
s=input()
print(s)
```

```python
Hello world!
```

- **文字列を複数の変数に格納する**

```python
1234
```

```python
a,b,c,d=input()
print(a,b,c,d)
```

```python
1 2 3 4
```

### 1 行 / C 列

- **整数を複数の変数に格納する**

```python
1 2
```

```python
a,b=map(int,input().split())
print(a)
print(b)
```

```python
1
2
```

- **文字列を複数の変数に格納する**

```python
Hello world!
```

```python
a,b=input().split()
print(a)
print(b)
```

```python
Hello
world!
```

- **リストに整数を格納する**

```python
1 2 3 4 5
```

```python
List=list(map(int,input().split()))
print(List)
```

```python
[1, 2, 3, 4, 5]
```

- **リストに文字列を格納する**

```python
Hello world !
```

```python
List=list(input().split())
print(List)
```

```python
['Hello', 'world', '!']
```

### R 行 / 1 列

- **整数を複数の変数に格納する**

```python
1
2
```

```python
a=int(input())
b=int(input())
print(a,b)
```

```python
1 2
```

- **リストに整数を格納する**

```python
1
2
3
4
5
```

```python
List=[int(input()) for i in range(5)]
print(List)
```

```python
[1, 2, 3, 4, 5]
```

- **リストに文字列を格納する**

```python
a
b
c
d
e
```

```python
List=[input() for i in range(5)]
print(List)
```

```python
['a', 'b', 'c', 'd', 'e']
```

- **入力行数が指定され、リストに整数を格納する**

```python
5
0
1
2
3
4
```

```python
Row=int(input())
List=[int(input()) for i in range(Row)]
print(List)
```

```python
[0, 1, 2, 3, 4]
```

- **入力行数が指定され、リストに文字列を格納する**

```python
5
a
b
c
d
e
```

```python
Row=int(input())
List=[input() for i in range(Row)]
print(List)
```

```python
['a', 'b', 'c', 'd', 'e']
```

### R 行 / C 列

- **整数を 2 次元リストに格納する**

```python
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
```

```python
List=[list(map(int,input().split())) for i in range(3)]
print(List)
```

```python
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
```

```python
3
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
```

```python
Row=int(input())
List=[list(map(int,input().split())) for i in range(Row)]
print(List)
```

```python
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
```

- **整数と文字列を複数のリストに格納する**

```python
3
0 a
1 b
2 c
```

```python
Row=int(input())
Number=[]
Alphabet=[]
for i in range(Row):
    n,a=input().split()
    Number.append(int(n))
    Alphabet.append(a)
print(Number)
print(Alphabet)
```

```python
[0, 1, 2]
['a', 'b', 'c']
```

## 03 数値計算

### a べき根 / 平方根

べき根は`**`演算子を使い`整数**べき根`とする。
計算結果は **浮動小数点数** となる。

```python
print(4**0.5)
2.0
```

```python
print(4**(1/2))
2.0
```

### b 階乗

階乗は`import math`で math ライブラリをインポートし、`math.factorial(整数)`となる。

```python
import math
print(math.factorial(5))
120
```

### c 小数点切り捨て

小数点切り捨て除法は `//` 演算子を使用する。除法の結果（商）は 整数(int)型 となる。

```python
print(5//3)

1
```

### d 小数点切り上げ

小数点切り上げ除法は`//`演算子を使用する。`-(-割られる数//割る数)`で小数点切り上げ除法となる。

```python
print(-(-5//3))

2
```

### e 剰余

剰余は`%`演算子を使用する。

```python
print(7%3)

1
```

## 04 条件文

### a if/elif/else 文

```python
a=1
if a==1:
    print("a is 1")
elif a==2:
    print("a is 2")
else:
    print("a is not 1 and 2")

a is 1
```

### b 三項演算

#### A if/else 文

条件式を三項演算で記述する場合、`print(条件式がTRUEの処理 if 条件式 else 条件式がFALSEの処理)`となる。

```python
a=1
print("a is 1" if a==1 else "a is not 1")

a is 1
```

#### B 複数条件式

条件式を複数組み合わせることができる。

```python
a=1
b=1
c=1
print("TRUE" if a==b==c else "FALSE")

TRUE
```

```python
a=1
b=2
c=3
d=4
print("TRUE" if a<b<c<d else "FALSE")

TRUE
```

## 05 繰り返し

### a for 文

for 文は`for 変数 in range(初期値,終了値):`となる。初期値を指定しない場合、`0`から始まる。

```python
for i in range(5):
    print(i)

0
1
2
3
4
```

```python
for i in range(2,5):
    print(i)
```

```python
2
3
4
```

### b while 文

while 文は`while 条件式:`となる。条件式が`TRUE`の場合、while 文の中の処理を続ける。

```python
i=0
while i<5:
    print(i)
    i=i+1
```

```python
0
1
2
3
4
```

## 06 整数（int）

- 整数（int）型の宣言は`int(データ)`となる
- 浮動小数点数型を整数型に変換した場合、**小数点が切り落とされる**

```python
print(int(2.9))
```

```python
2
```

- 整数か判定する

```python
f = 10.5
f.is_integer() #False
f = 10.0
f.is_integer() #True
```

## 07 文字列（str）

- 文字列の結合は`+`演算子を使用する
- 文字列の参照は`文字列[参照番号]`となる
- 文字列の比較は、整数と同様に行える
- 文字列の逆順は`文字列[::-1]`となる
- 文字列の長さは`len(str)`

### a 文字列の結合

文字列の結合は`+`演算子を使用する。

```python
print("foo"+"bar")
```

```python
foobar
```

---

```python
a="Fizz"
b="Buzz"
print(a+b)
```

```python
FizzBuzz
```

### b 文字列の参照（抽出）

文字列の参照は`文字列[参照番号]`となる。
参照番号に負の整数を指定すると、後ろからのインデックスになる

```python
String="abc"
print(String[0],String[1],String[2])
print(String[-3],String[-2],String[-1])
```

```python
a b c
a b c
```

### c 文字列の比較

文字列の比較は、整数と同様に行える。

```python
a="Hello"
b="Hello"
print("TRUE" if a==b else "FALSE")
```

```python
TRUE
```

```python
a="a"
b="b"
print("a<b" if a<b else "a>b")
```

```python
a<b
```

### d 文字列の逆順

```python
String="abc"
print(String[::-1])
```

```python
cba
```

### e 文字列の繰り返し

```python
b = [1, 2, 3] * 3
print(b)
```

```python
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### f 文字列のスライス

文字列は`[start:end:step]`で一部を取り出すことができる

- `[:]`は先頭から末尾までのシーケンス全体を抽出する
- `[start:]`は`start`から末尾までのシーケンスを抽出する
- `[:end]`は先頭から`end-1`オフセットまでのシーケンスを抽出する
- `[start:end]`は`start`から`end-`までのシーケンスを抽出する
- `[start:end:step]`は`step`文字ごとに`start`から`end`までのシーケンスを抽出する

```python
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[20:] == 'uvwxyz'
letters[10:] == 'klmnopqrstuvwxyz'

オフセット12から14を取り出す場合
letters[12:15] == 'klmnopqrstuvwxyz'

最後の3文字を取り出す
letters[-3:] == 'xyz'

末尾の6文字手前から3文字手前まで
letters[-6:-2] == 'uvwx'

先頭から末尾まで7文字ごとに抽出する
letters[::7] == 'ahov'

逆順にする
letters[::-1]
```

### g 文字列の分割

```python
a = 'ab c d e fgh ij'
a.split() == [ab,c,d,e,fgh,ij]
```

### h 大文字小文字の変換

```python
setup = 'a duck goed into a bar'

先頭の単語をタイトルケースにする
setup.capitalize()
    'A duck goes into a bar'

すべての単語をタイトルケースにする
setup.title()
    'A Duck Goes Into A Bar'

すべての文字を大文字にする
setup.upper()
    'A DUCK GOES INTO A BAR"

すべての文字を小文字にする
setup.lower()
    'a duck goes into a bar'

すべての大文字小文字を逆にする
setup.swapcase()
    'A DUCK GOES INTO A BAR'
```

### i 文字列の置換

```python
setup.replace('duck', 'marmoset')
duckがmarmosetに入れ替わる
```

## 08 リスト（list）

キーポイント

- 要素の追加は`append`メソッドを使用する
- 要素の追加は`リスト名.append(データ)`でリストの最後に追加される
- 要素の探索は`index`メソッドを使用する
- 要素の探索は`リスト名.index(データ)`でリストの先頭から探索され、一番初めに見つかったインデックスを返却する
- 要素の削除は`pop`メソッドを使用する
- 要素の削除は`リスト名.pop(要素番号)`で要素番号の要素が削除される
- 要素の削除で要素番号を指定しない`リスト名.pop()`とリストの最後の要素が削除される
- 要素の出現回数は`count`メソッドを使用する
- 要素の出現回数は`リスト名.count(データ)`で出現回数が返却される
- 要素のユニーク化はリスト`list`型から集合`set`型に変換することによって要素をユニークにできる
- スライスは`リスト名[最初のインデックス:最後のインデックス:ステップ数]`となる

### a 要素の追加

要素の追加は`append`メソッドを使用する。`リスト名.append(データ)`でリストの最後に追加される。

```python
List=["a","b","c"]
List.append('d')
print(List)
```

```python
['a', 'b', 'c', 'd']
```

```python
List=[0,1,2]
List.append(3)
print(List)
```

```python
[0, 1, 2, 3]
```

要素の挿入`insert`を用いてオフセットを指定して要素を追加できる

```python
List = [0,1,2]
List.insert(1,10)
print(List)
[0,10,1,2]
```

### b 要素の探索

要素の探索は`index`メソッドを使用する。`リスト名.index(データ)`でリストの先頭から探索され、一番初めに見つかったインデックスを返却する。

```python
List=["a","b","c","d","e","f"]
print(List.index('c'))
```

```python
2
```

```python
List=["a","b","c","d","c","c"]
print(List.index('c'))
```

```python
2
```

### c 要素の削除

要素の削除は`pop`メソッドを使用する。`リスト名.pop(要素番号)`で要素番号の要素が削除される。要素番号を指定しない`リスト名.pop()`と、リストの最後の要素が削除される。

```python
List=["a","b","c","d","e","f"]
print(List.pop(1))
print(List)
```

```python
b
['a', 'c', 'd', 'e', 'f']
```

```python
List=[1,2,3,4,5]
print(List.pop())
print(List)
```

```python
5
[1, 2, 3, 4]
```

`remove`による要素の削除

```python
List = ['ABC', 'DEF', 'GHI']
List.remove('DEF')
print(List)
['ABC','GHI']
```

### d 要素の出現回数

要素の出現回数は`count`メソッドを使用する。`リスト名.count(データ)`で出現回数が返却される。

```python
List=["a","b","b","c","c","c"]
print(List.count('c'))
```

```python
3
```

```python
List=["a","b","b","c","c","c"]
print(List.count('d'))
```

```python
0
```

### e 要素のユニーク化 重複削除

要素のユニーク化はリスト`list`型から集合`set`型に変換することによって要素をユニークにできる。ただし、要素の順序性は保たれない。

```python
List=[1,2,3,2,1,3]
print(list(set(List)))
```

```python
[1, 2, 3]
```

### f スライス

Python ではリストの一部を切り出せるスライスという機能がある。スライスは`リスト名[最初のインデックス:最後のインデックス:ステップ数]`となる。

```python
List=["a","b","c","d","e"]
print(List[1:3])
```

```python
['b', 'c']
```

```python
List=["a","b","c","d","e"]
print(List[1:4:2])
```

```python
['b', 'd']
```

```python
List=["a","b","c","d","e"]
print(List[:3])
```

```python
['a', 'b', 'c']
```

```python
List=["a","b","c","d","e"]
print(List[3:])
```

```python
['d', 'e']
```

### g 要素の結合

```python
a = ['a','b','c','d']
','.join(a) = 'a,b,c,d'

```

### h リストに含まれるか

`in`を用いてリストに値が含まれるかを調べられる

```python
a = ['a','b','c','d']
'd' in a == True
```

## 基本処理

第 3 章では基本処理（よく使われる関数とメソッド）について説明します。

## 01 長さ

キーポイント

- 文字列とリストの長さを得る場合、`len`関数を使用する
- 文字列とリストの長さを得る場合、`len(データ)`となる

### a 文字列の長さ

文字列の長さを得る場合、`len(変数名)`となる。

```python
String="aiueo"
print(len(String))
```

```python
5
```

### b リスト

リストの長さを得る場合、`len(リスト名)`となる。

```python
List=["a","b","c","a"]
print(len(List))

```

```python
4
```

## 02 ソート

- ソートをする場合、`sorted`関数を使用する
- ソートは昇順で行われる
- ソートを降順にする場合、`sorted(データ)[::-1]`となる

### a 昇順

ソートをする場合、`sorted`関数を使用する。ソートは昇順で行われる。

```python
List=[2,1,3]
print(sorted(List))
```

```python
[1, 2, 3]
```

### b 降順

ソートを降順にする場合、`sorted(データ)[::-1]`となる。

```python
List=[2,1,3]
print(sorted(List)[::-1])
```

```python
[3, 2, 1]
```

### c アルファベットの大文字小文字を区別せずソート

```python
a = ['e', 'B', 'd', 'C', 'a']
print(sorted(a))
print(sorted(a, key=lambda x: x.upper()))
```

```python
['B', 'C', 'a', 'd', 'e']['a', 'b', 'c', 'd', 'e']
```

### d 二個目の要素でソート

```python
w=[[1, 2], [2, 6] , [3, 6], [4, 5], [5, 7]]
w.sort()
w.sort(key=lambda x:x[1],reverse=True) #二個目の要素で降順並び替え
```

### e 多重キーでのソート

内部のタプルの 1 要素目（アルファベット），2 要素目（数字），0 要素目（数値）の順に比較してソート

```python
a = [(1, 'One', '1'), (1, 'One', '01'),
(2, 'Two', '2'), (2, 'Two', '02'),
(3, 'Three', '3'), (3, 'Three', '03')]
print(sorted(a, key=lambda x: (x[1], x[2], x[0])))
```

```python
[(1, 'One', '01'), (1, 'One', '1'), (3, 'Three', '03'), (3, 'Three', '3'), (2, 'Two', '02'), (2, 'Two', '2')]
```

## 03 最大値 / 最小値

キーポイント

- 最大値を得る場合、`max`関数を使用する
- 最小値を得る場合、`min`関数を使用する

### a 最大値

最大値を得る場合、`max`関数を使用する。

- 整数

整数の場合、`max(整数A,整数B)`となる。

```python
print(max(2,3))
```

```python
3
```

- 変数

変数の場合、`max(変数名A,変数名B,変数名C)`となる。

```python
a=1
b=2
c=3
print(max(a,b,c))
```

```python
3
```

- リスト

リストの場合、`max(リスト名)`となる。

```python
List=[2,4,6,8]
print(max(List))
```

```python
8
```

### b 最小値

最小値を得る場合、`min`関数を使用する。

- 整数

整数の場合、`min(整数A,整数B)`となる。

```python
print(min(2,3))
```

```python
2
```

- 変数

変数の場合、`min(変数名A,変数名B,変数名C)`となる。

```python
a=3
b=4
c=5
print(min(a,b,c))
```

```python
3
```

- リスト

リストの場合、`min(リスト名)`となる。

```python
List=[2,4,6,8]
print(min(List))
```

```python
2
```

## 04 合計値

キーポイント

- 合計値を得る場合、`sum`関数を使用する
- 合計値を得る場合、`sum(データ)`となる

```python
List=[1,2,3]
print(sum(List))
```

```python
6
```

### a 数字和

`map`関数を使用して、`sum(map(int,整数の文字列データ))`で数字和を求めることができる。

```python
x="1234"
print(sum(map(int,x)))
```

```python
10(=1+2+3+4)
```

## 05 集合

### a 和集合・積集合

```python
a = [2, 4, 6, 8]
b = [3, 6, 9]

print(list(set(a) | set(b))) # 和集合
print(list(set(a) & set(b))) # 積集合
```

```python
[2, 3, 4, 6, 8, 9][6]
```

## 06 絶対値

キーポイント

- 絶対値を得る場合、`abs`関数を使用する
- 絶対値を得る場合、`abs(数値データ)`となる

```python
print(abs(-1))
```

```python
1
```

## 07 置換

キーポイント

- 置換をする場合、`replace`メソッドを使用する
- 置換をする場合、`文字列.replace("置換前文字列","置換後文字列")`となる

```python
String="abcde"
print(String.replace("bc","xy"))
```

```python
axyde
```

## 08 大文字小文字変換

キーポイント

- 文字列を大文字に変換する場合、`upper`メソッドを使用する
- 文字列を大文字に変換する場合、`文字列.upper()`となる
- 文字列を小文字に変換する場合、`lower`メソッドを使用する
- 文字列を小文字に変換する場合、`文字列.lower()`となる

### a 大文字変換

文字列を大文字に変換するのは`upper`メソッドを使用する。`文字列.upper()`となる。

```python
Text="this is a pen."
print(Text.upper())
```

```python
THIS IS A PEN.
```

### b 小文字変換

文字列を小文字に変換するのは`lower`メソッドを使用する。`文字列.lower()`となる。

```python
Text="THIS IS A PEN."
print(Text.lower())
```

```python
this is a pen.
```

## 09 最大公約数・最小公倍数

```python
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b) 最大公約数
f2=a*b//f 公倍数
print(f,f2)
```

a,b,c の最大公約数は(a,b の公約数)と c の公約数に等しい

複数の数値の最小公倍数

```python
import functools
import fractions

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)

lcm_list(l)
```

## 10 n 進数

```python
i = 255
bin_str = format(i, 'b')# 11111111
oct_str = format(i, 'o')# 377
hex_str = format(i, 'x')# ff
```

```python
n=64
k=-3
bi=''
while n!=0:
bi+=str(n%abs(k))
if k<0:n=-(-n//k)
else:n=n//k
print(bi[::-1])
```

## 11 ゼロ埋め・幅寄せ

```python
print("python".ljust(15,'-')) # 左詰め
#python---------
print("python".center(15,'-'))# 中央寄せ
#-----python----
print("python".rjust(15,'-')) # 右詰め
#---------python

print(str(29).rjust(10,'0')) #10 桁ゼロ埋め
#0000000029
```

## 12 素数・約数・素因数

```python
#nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

```python
#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass #sortされていない
```

```python
#nの素因数分解(O(n**0.5)
def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass
```

```python
#[[素因数,数]]を出力
def fctr1(n):
    f=[]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    return f
```

```python
#n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass
```

```python
#a以上b未満の素数列挙
def segment_sieve(a,b):
    ass = []
    is_prime_small = [True] * (int(b**0.5)+1)
    is_prime = [True] * (b-a)
    for i in range(2,int(b**0.5)):
        if is_prime_small[i]:
            j = 2*i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2*i,((a+i-1)//i)*i)
            while j < b:
                is_prime[j-a] = False
                j += i
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(a+i)
    if ass[0] == 1:
        del ass[0]
    return ass
```

## 13 階乗・順列・組み合わせ

```python
# i の階乗
import math
math.factorial(i)

# 4P2
math.factorial(4) // math.factorial(4 - 2)

# 10C3
math.factorial(10) // math.factorial(10 - 3) // math.factorial(3)
```

## その他

## 01 代入演算

代入演算は下記の表の通りとなる。

| 演算子 | 記述例  |   意味   |
| :----: | :-----: | :------: |
|   +=   |  a+=b   |  a=a+b   |
|   -=   |  a-=b   |  a=a-b   |
|  \*=   |  a\*=b  |  a=a\*b  |
| \*\*=  | a\*\*=b | a=a\*\*b |
|   /=   |  a/=b   |  a=a/b   |
|  //=   |  a//=b  |  a=a//b  |
|   %=   |  a%=b   |  a=a%b   |

```python
a,b=1,2
a,b=b,a
print(a,b)
```

## 02 文字列定数

```python
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
```

```python
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
```

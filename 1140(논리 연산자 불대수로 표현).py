#논리 연산자(OR)
x, y=map(int, input().split())
b1=bool(x)#bool대수로 표현->참 또는 거짓을 나타냄
b2=bool(y)
r=int(b1 or b2)
print(r)

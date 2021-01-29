#비트 연산자(<<)
#<<는 a를 구성하고 있는 비트를 왼쪽으로 x번 이동한 후 결과 보여줌
a, x=map(int, input().split())
print("%d" %(a<<x))
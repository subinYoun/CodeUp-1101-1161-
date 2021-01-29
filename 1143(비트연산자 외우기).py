#비트 연산자(AND)
#두 정수를 비트단위로 and계산 후 10진수로 출력
a, b=map(int, input().split())
print("%d" %(a&b))
#비트단위 연산자: ~(not), &(and), |(or), ^(xor), <<(left shift), >>(right shift)
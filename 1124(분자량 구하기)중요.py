#분자량 구하기 ex)C3H8(입력)->44(출력)
a, b=input().split("H")#H로 나누어 두 개의 단어 입력
c=int(a[1:])#a에서 첫번째 한글자 제외
b=int(b)
print("%d" %(c*12+b))
a = int(input())
b = int(input())
c = int(input())
d = int(input())

filtred =  filter(lambda num: num % c == 0 and num % d == 0 , range(a, b + 1))
summa = sum(list(filtred))
print(summa)

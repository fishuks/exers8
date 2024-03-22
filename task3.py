a = int(input())
b = int(input())
c = int(input())
d = int(input())

numbers = list(range(a, b + 1))
list_of_values = list(map(lambda num : num % c != 0 and num % 10 == d, numbers))
count = 0
for i in range(len(list_of_values)):
    if list_of_values[i] == True:
        count += 1
print(count)

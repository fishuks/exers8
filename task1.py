def count_up(line, i, j):
    after_filtering = filter(lambda char: char.isupper(), line[i-1:j])
    return len(list(after_filtering))

line = input()
i = int(input())
j = int(input())

print(count_up(line, i, j))

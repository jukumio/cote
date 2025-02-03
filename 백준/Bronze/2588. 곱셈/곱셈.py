one = int(input())
two = int(input())
a = two % 10
b = two % 100 // 10
c = two % 1000 // 100
three = one * a

four = one * b

five = one * c

six = one * two

print(three, four, five, six, sep="\n")

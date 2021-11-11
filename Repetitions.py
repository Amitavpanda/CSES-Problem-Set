
s = input()
s = list(s)
p1 = 0
p2 = 1
count = 1
maximum = float("-inf")
if len(s) == 1:
    print(1)
else:
    while p2 < len(s):
        if s[p1] == s[p2]:
            p2 += 1
            count +=1
        else:
            count = 1
            p2 += 1
            p1 = p2 - 1
        if count > maximum:
            maximum = count
    print(maximum)

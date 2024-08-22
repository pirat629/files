f = open("17 (3).txt")
s = [int(i) for i in f]
b = []
k = 3567
summ = 0
start = 0
maxlen = 0
for i in range(len(s)):
    summ += s[i]
    while summ > k and start <= i:
        summ -= s[start]
        start += 1
    if summ == k:
        if len(s[start:i + 1]) > maxlen:
            b.clear()
            b.append(s[start:i + 1])
            maxlen = len(s[start:i + 1])
        elif len(s[start:i + 1]) == maxlen:
            b.append(s[start:i + 1])
maxi = 0
for i in range(len(b)):
    maxi = max(maxi, max(b[i]))
print(maxi)
f = open("17 (1).txt")
s = [int(i) for i in f]
summ = sum(s[:5])
maxi = 0
for i in range(5, len(s)):
    maxi = max(maxi, summ)
    summ = summ - s[i-5] + s[i]
print(maxi)
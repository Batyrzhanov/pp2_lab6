def div(n):
   for n in range(0, n+1):
   if (n%3==0) and (n%4==0):
            yield n

n = int(input())
for n in div(n):
    print(n, end=', ')
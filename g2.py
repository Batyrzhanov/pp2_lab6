def evenumbers(n):
return (str(x) for x in range(0, n + 1,2))

n = int(input())
result = evenumbers(n)
result_str = ', '.join(result)
print(result_str)
n = int(input())
s = -n // 4
print(-s)

n = int(input())
a = n % 10
b = (n % 100) // 10
c = n // 100
print(c, b, a, sep='')
print(c, a, b, sep='')
print(b, c, a, sep='')
print(b, a, c, sep='')
print(a, c, b, sep='')
print(a, b, c, sep='')

a, b, c = input()
print(a + b + c, a + c + b, b + a + c, b +
      c + a, c + a + b, c + b + a, sep='\n')


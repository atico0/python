def algo():
   yield 10
   yield 20
a = iter(range(100))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


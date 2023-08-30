#Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

fibonacci_gen = fib_gen()
for i in range(10):
    print(next(fibonacci_gen))
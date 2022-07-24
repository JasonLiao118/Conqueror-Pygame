from fibo import fib as fibonacci

new = [fibonacci.fib(1000)]

for x in new:
    print(x)
    if x == "1":
        break

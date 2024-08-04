
def caching_fibonacci() -> callable:
    cache = {} # створюємо словник для зберігання обчислень

    def fibonacci(n: int) -> int:
        if n <= 0: # якщо n <= 0, повертаємо 0
            return 0
        elif n == 1: # якщо n == 1, повертаємо 1
            return 1
        elif n in cache: # якщо n вже є у словнику, повертаємо його значення
            return cache[n]
        else:
            cache[n] = fibonacci(n -1) + fibonacci(n -2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))




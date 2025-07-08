def fizz_buzz(n):
    if n % 3:
        return "Fizz"
    elif n % 5:
        return "Buzz"
    elif n % 3 and n % 5:
        return "FizzBuzz"

n = int(input("Введите число: "))

print(fizz_buzz(n))


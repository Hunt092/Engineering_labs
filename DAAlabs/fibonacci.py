def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    count = int(input("Enter which fibonacci number you want: "))
    print(f'The {count}th fibonacci number is {fibonacci(count)}')

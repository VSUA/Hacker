try:
    n = int(input())
    denominator = int(input())

    print(n // denominator)
except:
    print("Division by zero is not supported")
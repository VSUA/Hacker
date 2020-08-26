number = int(input())

print(number.to_bytes(2, "big"))
print(number.to_bytes(2, "big")[1])

print(sum(number.to_bytes(2, "little")))


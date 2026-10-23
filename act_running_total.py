count = 0
total = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    count += 1
    total += price
    price = float(input("Price (0 to stop): "))

print(f"Items: {count} Total: {total:.2f}")

if count > 0:
    average = total / count
else:
    average = 0

correct_pin = "0803"
tries = 0

while tries < 3:
    pin = input("PIN: ")
    tries += 1

    if pin == correct_pin:
        print("Access granted")
        break

if tries == 3 and pin != correct_pin:
    print("Card blocked")

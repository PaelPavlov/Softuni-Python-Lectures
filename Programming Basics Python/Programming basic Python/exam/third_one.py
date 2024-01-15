upper_limit1 = int(input())
upper_limit2 = int(input())
upper_limit3 = int(input())

for digit1 in range(2, upper_limit1 + 1, 2):
    for digit2 in range(2, upper_limit2 + 1):
        for digit3 in range(2, upper_limit3 + 1, 2):
            is_prime = True
            for i in range(2, digit2):
                if digit2 % i == 0:
                    is_prime = False
                    break

            if is_prime:
                pin = f"{digit1}{digit2}{digit3}"
                print(pin)
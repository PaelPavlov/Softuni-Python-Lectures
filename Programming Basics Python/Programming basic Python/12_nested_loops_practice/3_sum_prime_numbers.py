prime_numbers_sum = 0
nonprime_numbers_sum = 0
command = input()
while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input() #Command = input() vinagi trqbva da prisystva predi continue
        continue
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += number
    else:
        nonprime_numbers_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {nonprime_numbers_sum}")

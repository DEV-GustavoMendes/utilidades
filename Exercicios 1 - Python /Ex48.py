
def prime_verification(number):

    prime = (number > 1) and all(number % i != 0 for i in range(2, int(number **0.5) + 1))

    if prime:
        print(f"{number} é primo.")
    else:
        print(f"{number} não é primo.")

prime_verification(8)
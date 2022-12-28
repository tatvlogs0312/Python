# todo: while
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done!")

secret_number = 9
guess_turn = 0
guess_limit = 3
while guess_turn < guess_limit:
    result = input("Guess: ")
    guess_turn += 1
    if int(result) == secret_number:
        print("you win")
        break
    if guess_turn == guess_limit:
        print("you lose")

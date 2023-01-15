def get_max(numbers):
    maxOfNumbers = numbers[0]
    for number in numbers:
        if number > maxOfNumbers:
            maxOfNumbers = number

    return maxOfNumbers

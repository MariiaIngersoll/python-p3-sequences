def print_fibonacci(length):
    sequence = []

    if length >= 1:
        sequence.append(0)
    if length >= 2:
        sequence.append(1)

    if length > 2:
        for i in range(2, length):
            sequence.append(
                sequence[i - 1] + sequence[i - 2])

    print(sequence)
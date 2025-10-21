while True:
    entry = input("Enter a number, or 'q' to quit: ")

    if entry == "q":
        break

    if not entry.isdigit():
        raise ValueError("That's not a valid number!")

    number = int(entry)
    print("=" * 40)
    i = 0
    while True:
        if i is number:
            print(f"Found it! i is {i}")
            break
        i += 1

        if i > 100_000:
            print("Giving up after 100,000 iterations")
            break

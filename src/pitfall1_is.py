from rich import print as rprint

while True:
    entry = input("Enter a number, or 'q' to quit: ")

    if entry == "q":
        break

    number = int(entry)
    rprint("=" * 40)
    i = -10
    while True:
        if i is number:
            rprint(f"Found it! i is {i}")
            break
        i += 1

        if i > 100_000:
            rprint("Giving up after 100,000 iterations")
            break

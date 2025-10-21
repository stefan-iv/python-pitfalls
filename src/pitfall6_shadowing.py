from rich import print as rprint
# Shadowing built-in names

sum = 0
for n in range(10):
    sum += n

print(f"sum={sum}")


numlist = list(range(5))
sum_of_numlist = sum(numlist)

rprint(f"Sum of {numlist} is {sum_of_numlist}")

from rich import print as rprint

# Truthiness or implied boolean conversion in Python refers to
# how different values are evaluated in a boolean context,
# such as in conditional statements. In Python, certain values are considered "truthy" (evaluating to True)
# and others are "falsy" (evaluating to False).


if 0:
    rprint("0 is truthy")
else:
    rprint("0 is falsy")


if 0.0:
    rprint("0.0 is truthy")
else:
    rprint("0.0 is falsy")


if []:
    rprint("Empty list is truthy")
else:
    rprint("Empty list is falsy")


if {}:
    rprint("Empty dict is truthy")
else:
    rprint("Empty dict is falsy")


config = {"host": "localhost", "port": 8080, "timeout": 0}


if not config.get("timeout"):
    rprint("No timeout configured (falsy)")


timeout = config.get("timeout")
rprint(f"Timeout is set to: {timeout} seconds")

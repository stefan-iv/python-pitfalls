from rich import print as rprint
import copy

original = {"users": ["alice", "bob"]}
rprint(f"Before copy: {original=}")
cloned = copy.copy(original)

cloned["users"].append("charlie")

rprint(f"After copy: {original=}")

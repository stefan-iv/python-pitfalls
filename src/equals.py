from rich import print as rprint

a = 5
b = int("5")
c = int("6")

print("Integer equality")
print("=" * 40)
rprint(f"{a=}, {b=}, {c=}")
rprint(f"a equals b: {a == b}")  # Should be True
rprint(f"a equals c: {a == c}")  # Should be False


rprint("\nString equality")
rprint("=" * 40)

s = "HELLO"
t = "HELLO"
u = "Y" + s[1:] + "W"

rprint(f"{s=}, {t=}, {u=}")
rprint(f"s equals t: {s == t}")  # Should be True
rprint(f"s equals u: {s == u}")  # Should be False


rprint("\nCustom object equality")
rprint("=" * 40)


class KeyValue:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"KeyValue(name='{self.name}', value='{self.value}')"


obj1 = KeyValue("k1", "obviously equal")
obj2 = KeyValue("k1", "obviously equal")
obj3 = KeyValue("k2", "obviously different")

rprint(f"obj1={obj1}\nobj2={obj2}\nobj3={obj3}")

rprint(f"obj1 equals obj2: {obj1 == obj2}")  # Should be True
rprint(f"obj1 equals obj3: {obj1 == obj3}")  # Should be False

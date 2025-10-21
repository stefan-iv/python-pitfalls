from rich import print as rprint


rprint("\nDemonstrating 'is' vs '==' with integers")


def is_vs_equal(a: int, b: int) -> None:
    rprint("=" * 40)

    rprint(f"{a=}, {b=}")
    rprint(f"id(a)={id(a)}, id(b)={id(b)}")

    if a is b:
        rprint("a is b")
    else:
        rprint("a is not b")

    if a == b:
        rprint("a equals b")
    else:
        rprint("a does not equal b")


is_vs_equal(5, int("5"))
is_vs_equal(1000, int("1000"))
is_vs_equal(256, int("256"))
is_vs_equal(-256, int("-256"))
is_vs_equal(257, int("257"))
is_vs_equal(-5, int("-5"))
is_vs_equal(-10, int("-10"))

is_vs_equal(10000, 10000)
is_vs_equal(10000, sum([5000, 5000]))

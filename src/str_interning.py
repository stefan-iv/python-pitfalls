from rich import print as rprint
# Python automatically interns some strings to optimize memory usage and performance.
# This means that identical string literals may refer to the same memory location.

# Strings that are automatically interned:
# 1. String literals that look like identifiers
#   Must contain only letters, digits, and underscores
#   Must not start with a digit
#   Examples: "hello", "my_var", "test123", "_private"
# 2. Empty string
#   "" is always interned
# 3. Single character strings (Latin-1 characters)
#   All single characters from the Latin-1 character set (0-255)
#   Examples: "a", "Z", "5", " " (space)
# 4. Compile-time constants
#   String concatenation with + at compile time
#   Example: "hello" + "world" (computed at compile time)


def check_string_interning(str1: str, str2: str) -> None:
    rprint(f"Comparing '{str1}' and '{str2}':")
    rprint(f"  id(str1) = {id(str1)}")
    rprint(f"  id(str2) = {id(str2)}")
    if str1 is str2:
        rprint("  They are the same object (interned).")
    else:
        rprint("  They are different objects.")
    rprint()


s1 = "hello_world"
s2 = "hello_world"
s3 = "hello_" + "world"
s4 = "".join(["hello", "_world"])


check_string_interning(s1, s2)
check_string_interning(s1, s3)
check_string_interning(s1, s4)
check_string_interning(s2, s4)

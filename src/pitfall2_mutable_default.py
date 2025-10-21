from rich import print as rprint


def validate_user(user: dict[str, str], errors: list[str] = []) -> list[str]:
    if not user.get("email"):
        errors.append("Missing email")
    if not user.get("age"):
        errors.append("Missing age")
    return errors


user1 = {"username": "alice"}
validation1 = validate_user(user1)

rprint("Validation errors for user:", user1)
rprint(validation1)

user2 = {"username": "bob", "email": "bob@example.com", "age": "30"}
validation2 = validate_user(user2)
rprint("Validation errors for user:", user2)
rprint(validation2)

custom_errors: list[str] = []
user3 = {"username": "charlie", "age": "25"}
validation3 = validate_user(user3, custom_errors)
rprint("Validation errors for user:", user3)
rprint(validation3)

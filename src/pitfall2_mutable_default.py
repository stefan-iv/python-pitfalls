from rich import print as rprint


def log_event(event: str, buffer: list[str] = []) -> list[str]:
    buffer.append(event)
    return buffer


rprint("=== Demonstrating Mutable Default Parameter ===")
print()

result1 = log_event("User login")
rprint(f"After 'User login': {result1}")
result2 = log_event("Page view")
rprint(f"After 'Page view': {result2}")
result3 = log_event("Button click")
rprint(f"After 'Button click': {result3}")


my_buffer: list[str] = []
result6 = log_event("Custom event 1", my_buffer)
rprint(f"Custom buffer after event 1: {result6}")

result7 = log_event("Custom event 2", my_buffer)
rprint(f"Custom buffer after event 2: {result7}")


rprint()
rprint("Back to default buffer (still has previous events):")
result8 = log_event("Another event")
rprint(f"Default buffer continues from before: {result8}")

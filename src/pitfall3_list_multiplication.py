from rich import print as rprint

matrix = [[0] * 3] * 3
rprint("Original matrix:")
rprint(matrix)


matrix[0][0] = 1
rprint("\nModified matrix (after setting matrix[0][0] = 1):")
rprint(matrix)

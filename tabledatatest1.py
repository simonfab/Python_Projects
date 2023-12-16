from tabulate import tabulate

data = [["Name", "Age", "City"],
        ["Alice", "24", "New York"],
        ["Bob", "27", "Los Angeles"],
        ["Charlie", "22", "Boston"]]

print(tabulate(data, headers="firstrow", tablefmt="grid"))
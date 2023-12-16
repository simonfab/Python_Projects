def validate_and_convert_input(input_string):
    try:
        cells_info = [int(cell) for cell in input_string.split(",") if cell in ['0', '1']]
        if len(cells_info) != len(input_string.split(",")):
            raise ValueError
        return cells_info
    except ValueError:
        print("Invalid input: Please enter 1s and 0s only, separated by commas.")
        return None

def process_cells(cells_info):
    freed_count = 0
    freed_list = []

    if cells_info[0] == 0:
        print("It's all over! - I'm locked in and nobody's getting out today!")
        return freed_count, freed_list

    for i in range(len(cells_info)):
        if cells_info[i] == 1:
            freed_list.append(f"Prisoner from cell {i + 1}")
            freed_count += 1
            cells_info = [1 - cell for cell in cells_info]  # Toggle all cells

        if all(cell == 0 for cell in cells_info[i+1:]):
            break

    return freed_count, freed_list

def main():
    input_string = input("Please enter each cell's lock status (1 = unlocked and 0 = locked) separated by commas: ")
    cells_info = validate_and_convert_input(input_string)
    if cells_info is not None:
        freed_count, freed_list = process_cells(cells_info)
        print("No more prisoners can be released")
        print("Final results:")
        print("Freed count =", freed_count)
        print("Freed prisoners:", ', '.join(freed_list))

if __name__ == "__main__":
    main()

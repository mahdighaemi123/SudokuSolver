import time

main_sudoku = [
    [[7, 0, 3], [6, 8, 0], [0, 5, 0]],
    [[0, 0, 8], [0, 0, 0], [0, 0, 0]],
    [[9, 0, 0], [0, 0, 4], [0, 6, 0]],

    [[3, 0, 0], [9, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, 5, 0], [0, 0, 8]],
    [[0, 0, 0], [0, 0, 8], [0, 0, 9]],

    [[0, 7, 0], [2, 0, 0], [0, 0, 1]],
    [[0, 0, 0], [0, 0, 0], [7, 0, 0]],
    [[0, 2, 0], [0, 1, 9], [3, 0, 6]]
]

# main_sudoku = [
#     [[8, 0, 0], [0, 0, 0], [0, 0, 0]],
#     [[0, 0, 3], [6, 0, 0], [0, 0, 0]],
#     [[0, 7, 0], [0, 9, 0], [2, 0, 0]],
#
#     [[0, 5, 0], [0, 0, 7], [0, 0, 0]],
#     [[0, 0, 0], [0, 4, 5], [7, 0, 0]],
#     [[0, 0, 0], [1, 0, 0], [0, 3, 0]],
#
#     [[0, 0, 1], [0, 0, 0], [0, 6, 8]],
#     [[0, 0, 8], [5, 0, 0], [0, 1, 0]],
#     [[0, 9, 0], [0, 0, 0], [4, 0, 0]]
# ]


def split_list(array, split_count):
    final_list = []

    for i in range(0, len(array)):
        index = i // split_count

        if index >= len(final_list):
            final_list.append([array[i]])
        else:
            final_list[index].append(array[i])

    return final_list


def print_sudoku(items):
    if not items:
        print("the imported sudoku is wrong")
        print()
        return

    item_3 = split_list(items, 3)
    rows = split_list(item_3, 3)

    for index, row in enumerate(rows):
        print(row)
        if (index + 1) % 3 == 0:
            print()


def get_all_items(rows):
    items = []
    rows = get_rows(rows)

    for row in rows:
        for item in row:
            items.append(item)

    return items


def get_squares(rows):
    squares = []
    items = get_all_items(rows)
    split_items = split_list(items, 3)

    for i in range(0, len(split_items) // 3):
        index = (i // 3 * 9) + i % 3
        squares.append([*split_items[index], *split_items[index + 3], *split_items[index + 3 + 3]])

    return squares


def justify_list(input_list):
    j_list = []

    for item in input_list:
        if isinstance(item, list):
            j_list = j_list + justify_list(item)
        else:
            j_list.append(item)

    return j_list


def get_rows(sudoku):
    rows = []

    for row in sudoku:
        row = justify_list(row)
        rows.append(row)

    return rows


def get_columns(rows):
    columns = []
    for i in range(0, 9):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)

    return columns


def is_solvent_sudoku(items, rows, columns):
    if not is_correct_columns(columns):
        return False

    if not is_correct_rows(rows):
        return False

    for i in items:
        if i == 0:
            return False

    return True


def can_solvent_sudoku(items):
    for i in items:
        if i == 0:
            return True

    return False


def is_correct_squares(squares):
    for square in squares:
        if not is_correct_square(square):
            return False

    return True


def is_correct_rows(rows):
    for row in rows:
        if not is_correct_row(row):
            return False
    return True


def is_correct_columns(columns):
    for column in columns:
        if not is_correct_column(column):
            return False
    return True


def is_correct_row(row):
    unique_array = make_unique_array(row)
    if len(unique_array) + get_zero_item_count(row) != 9:
        # print("Not Correct Row  -> ", row)
        return False
    else:
        # print("Correct Row  -> ", row)
        return True


def is_correct_column(column):
    unique_array = make_unique_array(column)
    if len(unique_array) + get_zero_item_count(column) != 9:
        # print("Not Correct Column  -> ", column)
        return False
    else:
        # print("Correct Column  -> ", column)
        return True


def is_correct_square(square):
    unique_square = make_unique_array(square)
    if len(unique_square) + get_zero_item_count(square) != 9:
        # print("Not Correct Square  -> ", square)
        return False
    else:
        # print("Correct Square  -> ", square)
        return True


def make_unique_array(array):
    unique_array = []

    for i in array:
        if i not in unique_array and i != 0:
            unique_array.append(i)

    return unique_array


def get_zero_item_count(array):
    count = 0

    for i in array:
        if i == 0:
            count += 1

    return count


def column_index_to_row_index(x, y):
    return y, x


def row_index_to_column_index(x, y):
    return y, x


def sudoku_solve(items):
    # print("Working ...")

    rows = split_list(items, 9)
    columns = get_columns(rows)
    squares = get_squares(rows)

    if not is_correct_columns(columns):
        return False

    if not is_correct_rows(rows):
        return False

    if not is_correct_squares(squares):
        return False

    if can_solvent_sudoku(items):

        for index, item in enumerate(items):

            if item == 0:

                for j in range(1, 10):
                    new_items = items.copy()
                    new_items[index] = j

                    result = sudoku_solve(new_items)

                    if result:
                        return result

                return False

    else:
        if is_solvent_sudoku(items, rows, columns):
            return items


print("Sudoku Solvent -> v1.0.0 ")
print()

print("Rows     -> ", get_rows(main_sudoku))
print("Columns  -> ", get_columns(get_rows(main_sudoku)))
print("Squares  -> ", get_squares(get_rows(main_sudoku)))
print()

print("is_correct_rows     -> ", is_correct_rows(get_rows(main_sudoku)))
print("is_correct_columns  -> ", is_correct_columns(get_columns(get_rows(main_sudoku))))
print("is_correct_squares  -> ", is_correct_squares(get_squares(get_rows(main_sudoku))))
print()

print("Working ...")
print()

start_time = time.time()

print_sudoku(sudoku_solve(get_all_items(get_rows(main_sudoku))))

end_time = time.time()
solve_time = end_time - start_time

print("Solve ;)")
print('Time Spent ->', time.strftime("%H:%M:%S", time.gmtime(solve_time)))


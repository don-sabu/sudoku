def isValidList(unique_list):
    if len(unique_list) != len(set(unique_list)):
        return False
    count = 0
    for i in unique_list:
        if 0 < i < 10:
            count += 1
    if count != 9:
        return False
    return True


def boxValid(table):
    for i in range(3):
        for j in range(3):
            box = []
            for x in range(i * 3, i * 3 + 3):
                for y in range(j * 3, j * 3 + 3):
                    box.append(table[x][y])
            if not isValidList(box):
                return False
    return True


def columnValid(table):
    for j in range(9):
        column = []
        for i in range(9):
            column.append(table[i][j])
        if not isValidList(column):
            return False
    return True


def rowValid(table):
    for row in table:
        if not isValidList(row):
            return False
    return True


def isValid(table):
    return rowValid(table) and columnValid(table) and boxValid(table)

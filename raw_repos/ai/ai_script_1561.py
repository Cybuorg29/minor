def select_columns(table, columns):
    output = [table[0]] + [[row[i] for i in columns] for row in table[1:]]
    return output
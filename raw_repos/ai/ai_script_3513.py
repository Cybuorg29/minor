def duplicate_rows(column, data):
    duplicates = []
    for row in data:
        if data[column].count(row[column]) > 1:
            duplicates.append(row)
    return duplicates
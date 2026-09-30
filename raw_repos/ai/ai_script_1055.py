def storeDataIn2DArray(data):
    rowLength = len(data[0])
    columnLength = len(data)
    twoDArray = []
  
    for row in range(rowLength):
        twoDArrayRow = []

        for column in range(columnLength):
            twoDArrayRow.append(data[column][row])

        twoDArray.append(twoDArrayRow)

    return twoDArray

def table_printer(tableData):
    column_width = len(max([x for i in tableData for x in i ], key=lambda k: len(k)))
    columns = len(tableData[0],)
    rows = len(tableData)
    for column in range(columns):
        res = []
        for row in range(rows):
            res.append(tableData[row][column].rjust(column_width))
        print(''.join(res))

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    table_printer(tableData)

class Matrix:
    def __init__(self, matrix_string):
        list_str = matrix_string.replace(' ', ',').replace('\n', ';')
        list = list_str.split(';')
        for i in range(len(list)):
            list[i] = list[i].split(',')
        for i in list:
            for j in range(len(i)):
                i[j] = float(i[j])

        self.listForm = list

    def row(self, index):
        return self.listForm[index-1]

    def column(self, index):
        column = []
        for i in self.listForm:
            column.append(i[index-1])
        return column

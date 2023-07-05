class MultiplicationTable:
    def __init__(self, size):
        self.size = size

    def define_larget_space(self):
        return str(len(str(self.size * self.size)) + 1)

    def create_table(self, row_no=0, column_no=0, start=1, exclude_list=None):
        if start < 1:
            raise Exception("Start must more than 1")
        if not row_no:
            row_no = self.size
        if not column_no:
            column_no = self.size
        data_x = [x for x in range(start, column_no+1)]
        data_y = [y for y in range(start, row_no+1)]
        new_data = list()
        for count, y in enumerate(data_y):
            temp = []
            for count2, x in enumerate(data_x):
                break_flag = False
                if exclude_list:
                    for coord_y, coord_x in exclude_list:
                        if count == coord_y-1 and count2 == coord_x-1:
                            temp.append(" ")
                            break_flag = True
                            break

                if not break_flag:
                    if count == 0 and count2 == 0:
                        temp.append(1)
                    if count == 0 and count2 > 0:
                        temp.append(x)
                    if count > 0 and count2 == 0:
                        temp.append(y)
                    if count > 0 and count2 > 0:
                        temp.append(x * y)
            new_data.append(temp)
        return new_data

    def setupSize(self, col=0, row=0, size=0):
        if not row:
            row = self.size
        if not col:
            col = self.size
        data_x = [x for x in range(1, col+1)]
        data_y = [y for y in range(1, row+1)]
        new_data = list()
        for count, y in enumerate(data_y):
            temp = []
            for count2, x in enumerate(data_x):
                if count == 0 and count2 == 0:
                    temp.append(1)
                if count == 0 and count2 > 0:
                    temp.append(x)
                if count > 0 and count2 == 0:
                    temp.append(y)
                if count > 0 and count2 > 0:
                    temp.append(x * y)
            new_data.append(temp)
        return new_data

    def printField(self, space, data):
        for row in data:
            for item in row:
                print(f"{str(item):>{space}}", end=" ")
            print()


class BaseCutTable(MultiplicationTable):
    x_v = []
    y_v = []

    def find_min(self):
        import math
        return math.ceil(self.size / 2)

    def cutJudge(self, x, y):
        return [x, y]

    def createCutTable(self):
        exclude_list = list()
        exclude_list.append([])
        data = self.create_table(exclude_list=exclude_list)
        space = self.define_larget_space()
        self.printField(space=space, data=data)


class CutTable(BaseCutTable):
    x_v = []
    y_v = []


class CutTable2(BaseCutTable):
    pass


q1a = CutTable(9)
q1a.createCutTable()
q1b = CutTable(15)
q1b.createCutTable()
q2a = CutTable2(8)
q2a.createCutTable()
q2b = CutTable2(17)
q2b.createCutTable()

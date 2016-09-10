class Calendar:
    cells = [[0 for i in range(7)] for j in range(5)]
    header = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def create(self):
        self.cells[0][4] = '1'
        self.cells[0][5] = '2'
        self.cells[0][6] = '3'
        self.cells[1][0] = '4'

if __name__ == '__main__':
    calendar = Calendar('2016', '08')
    calendar.create()
    [print(x) for x in calendar.cells]


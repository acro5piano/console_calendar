import calendar as cal
from termcolor import colored

class ConsoleCalendar:
    cells = [[0 for i in range(7)] for j in range(5)]
    header = ['Mo', 'Tu', 'We', 'Th', 'Fr', colored('Sa', 'blue'), colored('Su', 'red')]

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def print_on_console(self):
        month_name = cal.month_name[self.month]
        print(' '*int((len(month_name)/2 - 2)), cal.month_name[self.month], self.year)
        print(' '.join(self.header))
        print(self.calendar())

    def calendar(self):
        calendar_str = ''
        for week in cal.monthcalendar(self.year, self.month):
            calendar_str += self.format_week(week) + "\n"

        return calendar_str

    def format_week(self, week):
        week_str = ''

        for day in week:
            if day == 0:
                week_str += '   '
                continue

            wday =  cal.weekday(self.year, self.month, day)

            if wday == 5:
                week_str += colored(self.format_num(day), 'blue')
            elif wday == 6:
                week_str += colored(self.format_num(day), 'red')
            else:
                week_str += self.format_num(day)
            week_str += ' '

        return week_str

    def format_num(self, num):
        if 0 < num < 10:
            return ' ' + str(num)
        else:
            return str(num)


if __name__ == '__main__':
    calendar = ConsoleCalendar(2016, 9)
    calendar.print_on_console()

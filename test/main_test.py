from console_calendar.main import ConsoleCalendar
import pytest
from termcolor import colored

def test_calendar():
    calendar = ConsoleCalendar(2016, 8)
    expected = (
                ' 1  2  3  4  5 {0} {1} \n'.format(colored(' 6', 'blue'), colored(' 7', 'red')) +
                ' 8  9 10 11 12 {0} {1} \n'.format(colored('13', 'blue'), colored('14', 'red')) +
                '15 16 17 18 19 {0} {1} \n'.format(colored('20', 'blue'), colored('21', 'red')) +
                '22 23 24 25 26 {0} {1} \n'.format(colored('27', 'blue'), colored('28', 'red')) +
                '29 30 31             \n'
               )
    assert expected == calendar.calendar()


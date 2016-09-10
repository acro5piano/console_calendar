from console_calendar.main import Calendar

def test_initialize():
    calendar = Calendar('2016', '08')
    assert calendar != None


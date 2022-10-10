from datetime import datetime, timedelta
from calendar import HTMLCalendar

from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(event_date__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.title} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(event_date__year=self.year, event_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

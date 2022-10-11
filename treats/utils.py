from datetime import datetime, timedelta
from calendar import HTMLCalendar

from .models import Coupon


class Calendar(HTMLCalendar):
    """
    A calendar uses the coupon model to create events.
    An event is associated with a coupon recipient and one of the recipient's coupons.
    The title of the event should be the recipient's username.
    The description should be the treat associated with the coupon.
    Events should remain in the calendar after completed and be updated with visual representation for coupon state:
        - 1 week until target date: event in calendar turns yellow
        - past target date: event in calendar turns red
        - coupon fulfilled: events turns green
        - coupon expired: event turns gray
    """
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(target_date__day=day, recipient__isnull=False, treat__isnull=False)
        d = ''
        for event in events_per_day:
            d += f"<li> {event.recipient} - {event.treat.title} </li>"

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Coupon.objects.filter(target_date__year=self.year, target_date__month=self.month)

        breakpoint()

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar flex">'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

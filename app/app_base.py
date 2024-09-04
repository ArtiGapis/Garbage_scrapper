import src.works_template as works
from datetime import datetime


def get_garbage(trash):
    data = works.reader('../data/V. Tuinylos g.23.json')
    return data[trash]

def garbages_today(today):
    day = f'{today.year} {today.month} {today.day}'
    wrap = []
    for days in get_garbage("mixed"):
        if day in days:
            wrap.append('Mišrios atliekos')
    for days in get_garbage("paper"):
        if day in days:
            wrap.append('Popieriaus atliekos')
    for days in get_garbage("glass"):
        if day in days:
            wrap.append('Stiklo atliekos')
    return wrap

# Function to mark specific days by adding events with custom backgrounds
def mark_days(calendar):
    # Lists of dates to mark
    red_marked_dates, green_marked_dates = get_garbage('mixed'), get_garbage('paper')
    brown_marked_dates = get_garbage('glass')
    overlapping_dates = set()

    # Mark red dates (e.g., garbage collection days)
    for date_str in red_marked_dates:
        date_obj = datetime.strptime(date_str, '%Y %m %d').date()
        calendar.calevent_create(date_obj, 'Garbage Day', tags='red')

    # Mark green dates (e.g., recycling collection days)
    for date_str in green_marked_dates:
        date_obj = datetime.strptime(date_str, '%Y %m %d').date()
        if date_str in brown_marked_dates:
            overlapping_dates.add(date_str)
        else:
            calendar.calevent_create(date_obj, 'Garbage Day', tags='green')

    # Mark brown dates (e.g., recycling collection days)
    for date_str in brown_marked_dates:
        date_obj = datetime.strptime(date_str, '%Y %m %d').date()
        if date_str not in overlapping_dates:
            calendar.calevent_create(date_obj, 'Recycling Day', tags='brown')

    # Mark overlapping dates with a mixed color (e.g., orange for red + yellow)
    for date_str in overlapping_dates:
        date_obj = datetime.strptime(date_str, '%Y %m %d').date()
        calendar.calevent_create(date_obj, 'Both Events', tags='orange')

    # Configure the appearance of the tags
    calendar.tag_config('red', background='red', foreground='white')
    calendar.tag_config('green', background='green', foreground='white')
    calendar.tag_config('brown', background='brown', foreground='white')
    calendar.tag_config('orange', background='orange', foreground='black')



import datetime


def getLastWeek():

    today = datetime.date.today()
    start_last_week = today - datetime.timedelta(days=today.weekday(), weeks=1)
    return start_last_week


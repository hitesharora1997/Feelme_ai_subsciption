from datetime import timedelta, datetime


def calculate_end_date(start_date: datetime, duration: int) -> datetime:
    if not start_date:
        start_date = datetime.now()
    end_date = start_date + timedelta(days=30 * duration)
    return end_date

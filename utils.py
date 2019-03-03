from datetime import date


def get_date_from_string(date_string):
    date_string = date_string.split('-')

    return date(
        int(date_string[0]),
        int(date_string[1]),
        int(date_string[2]),
    )
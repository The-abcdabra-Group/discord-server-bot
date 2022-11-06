from datetime import timedelta


def convert_time(data: str):
    match data.lower()[-1]:
        case "d":
            return timedelta(days=int(data[:-1]))
        case "h":
            return timedelta(hours=int(data[:-1]))
        case "m":
            return timedelta(minutes=int(data[:-1]))
        case "s":
            return timedelta(seconds=int(data[:-1]))
        case _:
            raise ValueError("The time inputted is in an improper format!")

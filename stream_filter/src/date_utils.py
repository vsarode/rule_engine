from datetime import datetime


def get_date_from_string(value):
    return datetime.strptime(value,
                             '%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    value = get_date_from_string('2017-04-10 10:16:55')
    print(value)
    print(type(value))

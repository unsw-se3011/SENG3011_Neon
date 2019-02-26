#!python3
class FuzzTime(object):
    def __init__(self, datetime, month=0, day=0, hour=0, minute=0, sec=0):
        self.datetime = datetime
        self.data = [datetime.year, datetime.month,
                     datetime.day, datetime.hour, datetime.minute, datetime.second]
        print(self.data)

        self.data[0] = str(self.data[0])
        self.data[1:] = [t for t in map(
            lambda x: "%02d" % x, self.data[1:]
        )]

        print(self.data)
        # no fuzz
        fuzz_start = 6

        if month:
            fuzz_start = 1
        if day:
            fuzz_start = 2
        if hour:
            fuzz_start = 3
        if minute:
            fuzz_start = 4
        if sec:
            fuzz_start = 5
        for i in range(fuzz_start, 6):
            self.data[i] = 'xx'

    def __str__(self):
        return "-".join(self.data[:3]) + "T" + ":".join(self.data[-3:])


if __name__ == "__main__":
    import datetime

    dt = datetime.datetime.strptime('February 23, 2019', '%B %d, %Y')

    print(FuzzTime(dt, hour=True))
    print(FuzzTime(dt, day=True))
    print(FuzzTime(dt, month=True))
    print(FuzzTime(dt, sec=True))
    print(FuzzTime(dt))

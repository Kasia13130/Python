from datetime import datetime

def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

print("@" * 20)


def create_function(span="m"):

    if span == "m":
        sec = 60
    elif span == "h":
        sec = 3600
    elif span == "d":
        sec = 86400

    source = """
def f(start, stop):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
    """.format(sec)
    exec(source, globals())
    return f


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

f_minutes = create_function("m")
print(f_minutes(start, end))

f_hours = create_function("h")
print(f_hours(start, end))

f_days = create_function("d")
print(f_days(start, end))


def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(activity, obj):
    y_table = []
    for x in obj:
        y_table.append(activity(x))

    return y_table


x_table = list(range(11))

print("double: {} for: {}".format((generate_values(double, x_table)), x_table))
print("root: {} for: {}".format((generate_values(root, x_table)), x_table))
print("negative: {} for: {}".format((generate_values(negative, x_table)), x_table))
print("div2: {} for: {}".format((generate_values(div2, x_table)), x_table))


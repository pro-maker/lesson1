def get_summ(one, two, delimeter='&'):
    return str(one) + str(delimeter) + str(two)

one = "Learn"
two = "python"
a = get_summ(one, two)
print(a.upper())
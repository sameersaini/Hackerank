def sum_n(number):
    return (number * (number+1))//2


def sum_n_square(number):
    return (number * (number+1) * (2*number + 1))//6


print(sum_n(100)**2 - sum_n_square(100))

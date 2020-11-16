import matplotlib.pyplot as plt
from math import exp, factorial


def poisson_density(k, lmbd):
    return exp(-lmbd) * pow(lmbd, k) / factorial(k)


def poisson_distribution(k, lmbd):
    k = abs(k)
    sum = 0
    for i in range(k + 1):
        sum = sum + (pow(lmbd, i)) / factorial(i)
        if i == k:
            sum = sum * exp(-lmbd)
    return sum


def poisson(k_start, k_stop):
    lmbds = [1.0, 4.0, 10.0]
    for lmbd in lmbds:
        distribution_x = [i for i in range(k_start, k_stop + 1)]
        distribution_y = [poisson_distribution(x, lmbd) for x in distribution_x]
        prepare_show(distribution_x, distribution_y, "Пуассоновское распределение", "x", "F(x)")
    plt.show()

    for lmbd in lmbds:
        density_x = [i for i in range(k_start, k_stop + 1)]
        density_y = [poisson_density(x, lmbd) for x in density_x]
        prepare_show(density_x, density_y, "Пуассоновская плотность распределения", "x", "f(x)")
    plt.show()


def prepare_show(x_value, y_value, title, x_label, y_label):
    plt.plot(x_value, y_value)
    plt.grid(True)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)

    lab1 = u'λ=1'
    lab4 = u'λ=4'
    lab10 = u'λ=10'

    plt.legend((lab1, lab4, lab10))


poisson(0, 20)

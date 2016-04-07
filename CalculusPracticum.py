from math import sqrt
from math import exp
from math import fabs
from math import log

import inspect

eps, iterations_limit = 1e-13, 1000
init_x, alpha = float(input('Enter x: ')), float(input('Enter alpha: '))


def init_func(x_):
    return exp(alpha * fabs(x_)) - fabs(x_ ** 2 - alpha)


phi_pack = [
    lambda x: log(fabs(x ** 2 - alpha)) / alpha,
    lambda x: sqrt(fabs(alpha + exp(alpha * x))),
    lambda x: x * (exp(alpha * x) - x ** 2) / alpha,
    lambda x: (alpha + exp(alpha * x)) / x,
]

for ind, phi in enumerate(phi_pack):
    x = init_x
    i = 0
    dx = eps * 2  # should be > eps to enter 'while' loop
    func_x = eps * 2
    math_error = False

    print(inspect.getsource(phi)[14:-2])

    while dx > eps and fabs(func_x) > eps and i < iterations_limit:
        prev_x = x  # save old value of x

        try:
            x = phi(x)
            func_x = init_func(x)
        except Exception as err:
            math_error = True
            break

        i += 1
        dx = fabs(prev_x - x)

        # preparing report
        report = '\tx: {}  dx: {}  func(x): {}'.format(
            str(x).ljust(25),
            str(dx).ljust(25),
            str(func_x).ljust(25))

        # print(report)

    if i == iterations_limit:
        print('iterations limit reached!')
    elif math_error:
        print('math range reached!')
    elif i < iterations_limit:
        print('root: {}'.format(x))
        print('f(x): {}'.format(func_x))
        print('iterations: {}'.format(i))
    print('.' * 100)

# if i <= iterations_limit and dx < eps and func_x < eps:
#     report[ind]['status'] = 'success'
#     report[ind]['iterations'] = i
#     report[ind]['x'] = x
#     report[ind]['fx'] = func_x

# print()

from math import sqrt
from math import exp
from math import fabs
from math import log
import inspect

eps, iterations_limit = 1e-13, 1000
init_x, alpha = float(input('Enter x: ')), float(input('Enter alpha: '))


def write_report(report, show_log = False):
    str_array = []
    for ind, phi in enumerate(report):
        succeed = phi['status'] == 'success'
        str_array.append(
                '{status} - phi_{ind}: {phi}{in_case_of_success}'.format(
                        ind = ind,
                        phi = inspect.getsource(phi['phi'])[4:-2],
                        status = phi['status'],
                        in_case_of_success = ('\n\t{iter} iterations \n\tx = {x} \n\tf(x) = {fx}'
                                              .format(iter = phi['iterations'],
                                                      x = phi['x'],
                                                      fx = phi['fx']) if succeed else ''),
                )
        )
        if succeed and show_log:
            str_array.extend(phi['log'])
    return ''.join(map(lambda str: str + '\n', str_array))


def init_func(x_):
    return exp(alpha * fabs(x_)) - fabs(x_ ** 2 - alpha)


phi_pack = [
    lambda x: log(fabs(x ** 2 - alpha)) / alpha,
    lambda x: sqrt(fabs(alpha + exp(alpha * x))),
    lambda x: x * (exp(alpha * x) - x ** 2) / alpha,
    lambda x: (alpha + exp(alpha * x)) / x,
]

report = [
    {
        'status': 'fail',
        'iterations': 0,
        'x': None,
        'fx': None,
        'log': [],
        'phi': phi
    } for ind, phi in enumerate(phi_pack)
    ]

for ind, phi in enumerate(phi_pack):
    x, i = init_x, 0
    dx, func_x = eps * 2, eps * 2  # should be > eps to enter 'while' loop

    while dx > eps and fabs(func_x) > eps and i < iterations_limit:
        prev_x = x  # save old value of x

        try:
            x = phi(x)
            func_x = init_func(x)
        except Exception as err:
            break

        i += 1
        dx = fabs(prev_x - x)

        # preparing report
        report[ind]['log'].append('\tx: {}  dx: {}  func(x): {}'.format(
        # print('\tx: {}  dx: {}  func(x): {}'.format(
                str(x).ljust(25),
                str(dx).ljust(25),
                str(func_x).ljust(25)))

    if i <= iterations_limit and dx < eps and func_x < eps:
        report[ind]['status'] = 'success'
        report[ind]['iterations'] = i
        report[ind]['x'] = x
        report[ind]['fx'] = func_x

print(write_report(report, False))

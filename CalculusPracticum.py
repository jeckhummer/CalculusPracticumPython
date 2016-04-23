from math import sqrt
from math import exp
from math import fabs
from math import log

import inspect

eps, iterations_limit = 1e-13, 1000
init_x, alpha = float(input('Enter x: ')), float(input('Enter alpha: '))

print('\n')

def init_func(x_):
    return exp(alpha * fabs(x_)) - fabs(x_ ** 2 - alpha)


phi_pack = [
    lambda x: log(fabs(alpha - x*x))/ alpha,
    lambda x: sqrt(fabs(alpha + exp(alpha * x))),
    lambda x: x * (exp(alpha * x) - x ** 2) / alpha,
    # lambda x: (alpha + exp(alpha * x)) / x,
]

report = ''

for ind, phi in enumerate(phi_pack):

    x = init_x
    i = 0
    dx = eps * 2  # should be > eps to enter 'while' loop
    func_x = eps * 2

    # errors
    math_error = False
    has_error = False
    not_root_error = False
    iterations_limit_error = False

    report_flag = False
    report_flag = True

    replace_alpha = True
    # replace_alpha = False

    inline_report = False
    # inline_report = True

    report += '{}. '.format(ind + 1)

    if not inline_report:
        report += '{}\n'.format(inspect.getsource(phi)[14:-2]).replace('alpha', str(alpha) if replace_alpha else 'alpha')

    if not inline_report and report_flag:
        report += '\n\tx: {}  dx: {}  func(x): {}'.format(
            str(x).ljust(25),
            str(dx).ljust(25),
            str(func_x).ljust(25))

    while dx > eps and fabs(func_x) > eps and i < iterations_limit:
        prev_x = x  # save old value of x

        try:
            x = phi(x)
            func_x = init_func(x)
        except Exception as err:
            math_error = True
            has_error = True
            break

        i += 1
        dx = fabs(prev_x - x)

        # preparing report
        if not inline_report and report_flag:
            report += '\n\tx: {}  dx: {}  func(x): {}'.format(
                str(x).ljust(25),
                str(dx).ljust(25),
                str(func_x).ljust(25))

    if not inline_report and report_flag:
        report += '\n'

    if i == iterations_limit:
        iterations_limit_error = True
        has_error = True

    if fabs(func_x) > 0.0001:
        not_root_error = True
        has_error = True

    if has_error:
        if inline_report:
            report += '--\n'
        else:
            report += '\n'

            if iterations_limit_error:
                report += 'iterations limit reached!'
            elif math_error:
                report += 'math range reached!'
            elif not_root_error:
                report += 'point of convergence is not root! f(x): {}'.format(func_x)

            report += '\n'
    else:
        if inline_report:
            report += '{}\n'.format(x)
        else:
            report += '\nroot: {}'.format(x)
            report += '\nf(x): {}'.format(func_x)
            report += '\niterations: {}'.format(i)

    if not inline_report:
        report += '\n' + '.' * 100 + '\n'

print(report)

# if i <= iterations_limit and dx < eps and func_x < eps:
#     report[ind]['status'] = 'success'
#     report[ind]['iterations'] = i
#     report[ind]['x'] = x
#     report[ind]['fx'] = func_x

# print()

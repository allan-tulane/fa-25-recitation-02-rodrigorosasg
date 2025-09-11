import tabulate
import time

def _next_size(n, b):
    return max(1, n // b)

def simple_work_calc(n, a, b):
    if n <= 1:
        return 1
    return a * simple_work_calc(_next_size(n, b), a, b) + n

def work_calc(n, a, b, f):
    if n <= 1:
        return 1
    return a * work_calc(_next_size(n, b), a, b, f) + f(n)

def span_calc(n, a, b, f):
    if n <= 1:
        return 1
    return span_calc(_next_size(n, b), a, b, f) + f(n)

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    result = []
    for n in sizes:
        result.append((n, work_fn1(n), work_fn2(n)))
    return result

def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['n', 'W_1', 'W_2'],
                            floatfmt=".3f",
                            tablefmt="github"))

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    result = []
    for n in sizes:
        result.append((n, span_fn1(n), span_fn2(n)))
    return result

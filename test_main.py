import math
from main import simple_work_calc, work_calc, span_calc, compare_work, compare_span

def test_simple_work():
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230
    assert simple_work_calc(30, 4, 2) == 650

def test_simple_work_more():
    assert simple_work_calc(1, 5, 7) == 1
    assert simple_work_calc(5, 2, 3) == 7
    assert simple_work_calc(50, 2, 5) == 86

def test_work():
    assert work_calc(10, 2, 2, lambda n: 1) == 15
    assert work_calc(20, 1, 2, lambda n: n*n) == 530
    assert work_calc(30, 3, 2, lambda n: n) == 300

def test_work_more():
    assert work_calc(10, 1, 2, lambda n: n*n) == 130
    assert work_calc(10, 3, 2, lambda n: 1) == 40
    assert work_calc(16, 2, 2, lambda n: n) == 80

def test_compare_work():
    work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n)
    work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: 1)
    sizes = [10, 50, 100, 1000]
    res = compare_work(work_fn1, work_fn2, sizes=sizes)
    for (n, w1, w2) in res:
        assert w1 > w2
    n, w1, w2 = res[2]
    assert n == 100 and w1 == work_fn1(100) and w2 == work_fn2(100)

def test_span_values():
    assert span_calc(16, 2, 2, lambda n: 1) == 5
    assert span_calc(16, 2, 2, lambda n: n) == 31
    assert span_calc(16, 2, 2, lambda n: int(math.log(n, 2)) if n > 1 else 0) == 11

def test_compare_span():
    s_n   = lambda n: span_calc(n, 2, 2, lambda n: n)
    s_one = lambda n: span_calc(n, 2, 2, lambda n: 1)
    res = compare_span(s_n, s_one, sizes=[8, 16, 32])
    for (n, s1, s2) in res:
        assert s1 > s2

import numpy


def hello(n: int) -> str:
    sum_n = numpy.arange(n).sum()
    return f"Hello {sum_n}!"

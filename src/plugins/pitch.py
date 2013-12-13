import numpy


def pitch_up(data):
    low_freq = 30
    zeros = numpy.ndarray(low_freq/2, dtype=numpy.complex128)
    cnt = numpy.concatenate([zeros, data])[:len(data)]
    return cnt


def pitch_down(data):
    low_freq = 80
    zeros = numpy.ndarray(low_freq/2, dtype=numpy.complex128)
    cnt = numpy.concatenate([data, zeros])[len(zeros):]
    return cnt

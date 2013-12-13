# -*- coding: utf-8 -*-
import numpy
import scipy.fftpack as fft


class Transformer(object):
    def __init__(self, filter_):
        self.filter_ = filter_


    def transform(self, data):
        data = numpy.frombuffer(data, dtype=numpy.int16)
        f = fft.fft(data)
        left, right = f[:len(f)/2], f[len(f)/2:]
        transformed = []
        for ch in (left, right):
            transformed.extend(self.filter_(ch))
            #transformed.extend(ch)
        rev = fft.ifft(transformed)
        out_data = numpy.getbuffer(rev.astype(numpy.int16))
        #out_data = rev
        return out_data

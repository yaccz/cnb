#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from .controller import getRates

class Wrapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.rates = None

    def set_rates(self, rates):
        self.rates = rates

    def __getattr__(self, name):
        try:
            return getattr(self.wrapped, name)
        except AttributeError:
            if not self.rates:
                getRates(self.set_rates)
            return self.rates[name]

sys.modules[__name__] = Wrapper(sys.modules[__name__])

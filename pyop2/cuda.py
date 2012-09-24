# This file is part of PyOP2
#
# PyOP2 is Copyright (c) 2012, Imperial College London and
# others. Please see the AUTHORS file in the main source directory for
# a full list of copyright holders.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * The name of Imperial College London or that of other
#       contributors may not be used to endorse or promote products
#       derived from this software without specific prior written
#       permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTERS
# ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import runtime_base as op2
from runtime_base import Set, IterationSpace, Sparsity
from utils import verify_reshape

class Kernel(op2.Kernel):
    def __init__(self, code, name):
        op2.Kernel.__init__(self, code, name)

class DeviceDataMixin:
    def fetch_data(self):
        return self._data

class Dat(op2.Dat, DeviceDataMixin):
    def __init__(self, dataset, dim, data=None, dtype=None, name=None, soa=None):
        op2.Dat.__init__(self, dataset, dim, data, dtype, name, soa)
        self._on_device = False

class Mat(op2.Mat, DeviceDataMixin):
    def __init__(self, datasets, dtype=None, name=None):
        op2.Mat.__init__(self, datasets, dtype, name)
        self._on_device = False

class Const(op2.Const, DeviceDataMixin):
    def __init__(self, dim, data, name, dtype=None):
        op2.Const.__init__(self, dim, data, name, dtype)
        self._on_device = False

class Global(op2.Global, DeviceDataMixin):
    def __init__(self, dim, data, dtype=None, name=None):
        op2.Global.__init__(self, dim, data, dtype, name)
        self._on_device = False

    @property
    def data(self):
        self._data = self.fetch_data()
        return self._data

    @data.setter
    def data(self, value):
        self._data = verify_reshape(value, self.dtype, self.dim)
        self._on_device = False

class Map(op2.Map):
    def __init__(self, iterset, dataset, dim, values, name=None):
        op2.Map.__init__(self, iterset, dataset, dim, values, name)
        self._on_device = False

def par_loop(kernel, it_space, *args):
    pass

def _setup():
    pass

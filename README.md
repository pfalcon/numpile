Numpile
-------

A tiny 1000 line LLVM-based numeric specializer for scientific Python code.

You really shouldn't use this for anything serious, it's just to demonstrate how
you might build one of these things from scratch. There's a lot of untapped
potential and low hanging fruit around *selective embedded JIT specialization*
for array expression languages in the SciPython space.

Installing
----------

Numpile requires ``numpy`` and ``llvmlite`` (the latter includes needed
LLVM libraries). You can either try to install them using your OS package
manager, or alternatively, using ``pip``:

```bash
$ pip install llvmlite
$ pip install numpy
```

Usage
-----

```python
from numpile import autojit

@autojit
def dot(a, b):
    c = 0
    n = a.shape[0]
    for i in range(n):
       c += a[i]*b[i]
    return c

a = np.array(range(1000,2000), dtype='int32')
b = np.array(range(3000,4000), dtype='int32')

print dot(a,b)
```

License
-------

Released under the MIT License.
Copyright (c) 2015, Stephen Diehl

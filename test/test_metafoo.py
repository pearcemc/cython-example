import os
import sys 
sys.path.insert(0, os.path.abspath('..'))

import src.foo as foo
import src.metafoo as metafoo

lotsafoo = [foo.Foo(i) for i in range(4)]

mf = metafoo.MetaFoo(lotsafoo)
mf.special_print()

import os
import sys 
sys.path.insert(0, os.path.abspath('..'))

import src.foo as foo

somefoo = foo.Foo(2)
somefoo.special_print()

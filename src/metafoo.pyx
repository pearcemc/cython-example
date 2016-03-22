import os, sys 
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("../"))

cimport src.foo as foo

cdef class MetaFoo:
    cdef:
        list lotsafoo

    def __cinit__(MetaFoo self, list lotsafoo):
        self.lotsafoo = lotsafoo

    def special_print(MetaFoo self):
        cdef long i, n 
        cdef foo.Foo thisfoo
        n = len(self.lotsafoo)
        for i in range(n):
             thisfoo = self.lotsafoo[i]
             thisfoo.special_print()

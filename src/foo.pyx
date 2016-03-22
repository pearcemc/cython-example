#contents of cyproj/src/foo.pyx
import os, sys
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("../"))

from libc.stdlib cimport malloc, realloc, free

cdef class Foo:

    def __cinit__(Foo self, long n):
        cdef foo* thisfoo = <foo*> malloc(sizeof(foo))
        thisfoo.somefield = n
        self.myfoo = thisfoo
       
    cpdef void special_print(Foo self):
        print "The value of somefield is: %i" % self.myfoo.somefield 
    

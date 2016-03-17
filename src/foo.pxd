#contents of cyproj/src/foo.pxd

cdef struct foo:
    long somefield

cdef class Foo:
     cdef:
         foo* myfoo
 
     cpdef void special_print(Foo self)

import foo
import metafoo

lotsafoo = [foo.Foo(i) for i in range(4)]

mf = metafoo.MetaFoo(lotsafoo)
mf.special_print()

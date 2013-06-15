"""
An inspection of python reference counting

From:
http://pymotw.com/2/sys/limits.html
"""

#reference counting
import sys
one = []
print 'At start         :', sys.getrefcount(one)

two = one

print 'Second reference :', sys.getrefcount(one)

del two
print 'After del        :', sys.getrefcount(one)

#object size

class OldStyle:
    pass

class NewStyle(object):
    pass

for obj in  [ [], (), {}, 'c', 'string', 1, 2.3, OldStyle, OldStyle(),
              NewStyle, NewStyle()]:
    print '%10s : %s' % (type(obj).__name__, sys.getsizeof(obj))

class WithoutAttributes(object):
    pass

class WithAttributes(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return

without_attrs = WithoutAttributes()
print 'WithoutAttributes:', sys.getsizeof(without_attrs)

with_attrs = WithAttributes()
print 'WithAttributes:', sys.getsizeof(with_attrs)

#this gives a false sense of the amount of memory being consumed.
#for something more accurate of memory counts, within a given object
#better to do the following:

class WithAttributes2(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return
    def __sizeof__(self):
        return object.__sizeof__(self) + \
            sum(sys.getsizeof(v) for v in self.__dict__.values())


without_attrs = WithoutAttributes()
print 'WithoutAttributes:', sys.getsizeof(without_attrs)

with_attrs2 = WithAttributes2()
print 'WithAttributes2:', sys.getsizeof(with_attrs2)

#working with recursion


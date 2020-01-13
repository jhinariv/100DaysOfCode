from collections import namedtuple as cnt
from collections import deque as cdq
from collections import Counter as cct
from collections import ChainMap as ccm
import os
import argparse
from collections import OrderedDict as cod

# namedtuple() - factory function for creating tuple subclasses with named fields
EmployeeRecord = cnt('EmployeeRecord', 'name, age, title, department, paygrade')
e = EmployeeRecord(name='Bruno', age='16', title='coder', department='3', paygrade='200')
# print(e)
# print(e.age)
# print(f'{e.name} is a {e.title}')
# no es necesario colocoar a cual valor corresponde
e = EmployeeRecord('Alice', '16', 'coder', '9', '500')
# print(e)
# print(e.department)
# print(f'{e.name} is a {e.paygrade}')

Point = cnt('Point', 'x,y')
t = [11, 22]
p = Point._make(t)
# print(p)


# deque - list-like container with fast appends and pops on either end
d = cdq('ghi')
p# print(d)
d.append('j')
# print(d)
d.appendleft('a')
# print(d)
d2 = d.copy()
# print(d2)

# Counter - dict subclass for counting hashable objects
c = cct(['a', 'c'])
print(c['a'])
print(c['c'])
print(c['b'])

cmc = cct('abracadabra').most_common(3)
print(cmc)

# ChainMap - dict-like class for creating a single view of multiple mappings

b = {'music': 'bach', 'art': 'rembrandt'}
b2 = {'art': 'van gogh', 'opera': 'carmen'}
c = list(ccm(b2, b))
print(c)

a = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
b = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ccm(b, os.environ, a)
print(combined['color'])

# OrderedDict - dict subclass that remembers the order entries were added

d = cod.fromkeys('abcde')
d.move_to_end('b')
print(d)
d.popitem()
print(d)

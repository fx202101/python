l = ['Alice', 'Bob', 'Charlie']
d = {s: len(s) for s in l}
print(d)


keys = ['k1', 'k2', 'k3']
values = [1, 2,4]
d = {k: v for k, v in zip(keys, values)}
print(d)

l = [i**2 for i in range(5)]
print(l)
# [0, 1, 4, 9, 16]

from ast import Num
from datetime import date
from typing import Tuple
def sample() -> Tuple[list, str]:
    sample_list = [0, 1, 2, 3]
    sample_str = "tuple_return_test"
    return sample_list, sample_str
return_sample_list, return_sample_str = sample()
print(return_sample_list)
print(return_sample_str)

import re
l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']
l_re_match = [s for s in l if re.match('.*XXX.*', s)]
print(l_re_match)


myset1 = set([1,2,3])
myset2 = set([1,2,3,3,2,1])
print(myset1)
print(myset2)


#辞書からクラスに変換する
#asdictでdictに変換しています。
from dataclasses import asdict, dataclass
@dataclass
class Data:
    foo: int
    bar: int
dict1 = {'foo': 10, 'bar': 20}
data = Data(**dict1)
print(data.bar,data.foo)



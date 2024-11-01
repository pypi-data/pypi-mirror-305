# from typing import TYPE_CHECKING
from ovld import ovld
from ovld.core import OvldMC

# from plum import dispatch as ovld
# from multimethod import multimethod as ovld
# from runtype import multidispatch as ovld

# # if TYPE_CHECKING:
# from typing import overload


class O(metaclass=OvldMC):
    def f(self, x: int):
        pass

    def f(self, x: str):
        pass


@ovld
def f(x: int) -> int:
    "A"
    return x * x


@ovld
def f(x: str) -> int:
    "COX"
    return int(x)


f
print(f(8))
print(f("8"))
print(f([]))

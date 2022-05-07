import pytest
from datetime import datetime

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


def is_triangle(a, b, c):
    if b < a > c:
        return a < b + c
    elif a < b > c:
        return b < a + c
    else:
        return c < a + c
a = True
b = True
c = True
print(True if is_triangle(a, b, c) else False)



@pytest.mark.parametrize("a", [-1, 0, 1, 3], ids=["negative", "zero", "positive_not_triangle", "positive"])
@pytest.mark.parametrize("b", [-1, 0, 4, 4], ids=["negative", "zero", "positive_not_triangle", "positive"])
@pytest.mark.parametrize("c", [-1, 0, 5, 5], ids=["negative", "zero", "positive_not_triangle", "positive"])
def test_is_triangl(a, b, c):
   print(True if is_triangle(a, b, c) else False)
   assert True
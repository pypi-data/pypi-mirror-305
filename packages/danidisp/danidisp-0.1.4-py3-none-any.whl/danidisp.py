from time import perf_counter, sleep
from sys import stdout

def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x,y in zip(a,b)])

def dlog(n: int, b: int, mod: int) -> int:
    i = 0
    while True:
        if b**i % mod == n % mod:
            return i
        i += 1

def base_conv(n: str, bs: int = 10, be: int = 10) -> str:
    assert type(n) == type(''), 'Number must be a string.'
    n = n.lower()
    for ch in n:
        if ch.isnumeric():
            assert int(ch) < bs, 'Invalid number'
        elif 97 <= ord(ch) <= 122:
            assert ord(ch) - 97 + 10 < bs, 'Invalid number'
        else:
            raise AssertionError('Invalid number')
    if bs == be:
        return n
    assert 2 <= bs <= 35 and 2 <= be <= 35, 'Base must be inside [2,35] range.'
    if bs == 10:
        num = int(n)
        res = []
        while num > 0:
            res.append(num % be)
            num //= be
        res = [str(el) if el < 10 else chr(97 + el - 10) for el in res[::-1]]
        return ''.join(res)
    elif be == 10:
        nums = [int(el) if el.isnumeric() else ord(el) - 97 + 10 for el in n][::-1]
        res = 0
        for i, num in enumerate(nums):
            res += num * (bs**i)
        return str(res)
    else:
        return base_conv(base_conv(n, bs, 10), 10, be)
    
def clock(func, *args, **kwargs):
    def _clock(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        print('{0} took {1:.8f}s'.format(func.__name__, end-start))
        return res

    return _clock

GAP_TIME = 0.03

def sprint(string: str, gap: float = GAP_TIME, new_line: bool = True) -> None:
    for ch in string:
        stdout.write(ch)
        stdout.flush()
        sleep(gap)
    if ch != '\n' and new_line:
        stdout.write('\n')
        stdout.flush()

def sinput(prompt: str) -> str:
    sprint(prompt, new_line=False)
    return input()

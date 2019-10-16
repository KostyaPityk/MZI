import copy
from constants import H
import binascii
import random
from itertools import chain
from math import ceil, floor

class stb:
    @staticmethod
    def get_oct(value):
        if type(value) is not str:
            raise Exception("Value not string")
        return [ord(item) for item in value]

    def new_RotHi(self, value):
        return self.new_ShHi(value) ^ self.new_ShLo(value)

    @staticmethod
    def new_ShHi(value, k=1):
        return (value << k) ^ 2 ** 32

    @staticmethod
    def new_ShLo(value, k=31):
        return value >> k

    @staticmethod
    def to_int(values):
        shift = [24, 16, 8, 0]
        return sum([values[i] << shift[i] for i in range(4)])

    @staticmethod
    def to_list(value):
        shift = [24, 16, 8, 0]
        return [value >> item & 0xFF for item in shift]

    @staticmethod
    def to_int_l(values):
        shift = [0, 8, 16, 24]
        return sum([values[i] << shift[i] for i in range(4)])

    @staticmethod
    def to_list_l(value):
        shift = [0, 8, 16, 24]
        return [value >> item & 0xFF for item in shift]

    def plus(self, *args, base=2 ** 32):
        res = self.rev(args[0])
        for item in args[1:]:
            res = (res + self.rev(item)) % base
        return self.rev(res)

    def minus(self, a, b, base=2 ** 32):
        return self.rev((self.rev(a) - self.rev(b)) % base)

    def G(self, x, k):
        result = self.to_int([H(item) for item in self.to_list(x)])
        # result = self.rev(result)

        for _ in range(k):
            result = self.rev(self.new_RotHi(self.rev(result)))

        return result

    def encode(self, block, key):
        a, b, c, d, = [self.to_int(block[i : i + 4]) for i in range(0, len(block), 4)]
        keys = [self.to_int(key[i : i + 4]) for i in range(0, len(key), 4)]
        k = [keys[i % 8] for i in range(56)]
        for i in range(8):
            b = b ^ self.G(self.plus(a, k[7 * i + 0]), 5)
            c = c ^ self.G(self.plus(d, k[7 * i + 1]), 21)
            a = self.minus(a, self.G(self.plus(b, k[7 * i + 2]), 13))
            e = self.G(self.plus(self.plus(b, c), k[7 * i + 3]), 21) ^ self.to_int_l(
                self.to_list(i + 1)
            )
            b = self.plus(b, e)
            c = self.minus(c, e)
            d = self.plus(d, self.G(self.plus(c, k[7 * i + 4]), 13))
            b = b ^ self.G(self.plus(a, k[7 * i + 5]), 21)
            c = c ^ self.G(self.plus(d, k[7 * i + 6]), 5)
            a, b = b, a
            c, d = d, c
            b, c = c, b

        _a = self.to_list(a)
        _b = self.to_list(b)
        _c = self.to_list(c)
        _d = self.to_list(d)
        return _b + _d + _a + _c

    def decode(self, block, key):
        a, b, c, d, = [self.to_int(block[i : i + 4]) for i in range(0, len(block), 4)]
        keys = [self.to_int(key[i : i + 4]) for i in range(0, len(key), 4)]
        k = [keys[i % 8] for i in range(56)]
        for i in reversed(range(8)):
            b = b ^ self.G(self.plus(a, k[7 * i + 6]), 5)
            c = c ^ self.G(self.plus(d, k[7 * i + 5]), 21)
            a = self.minus(a, self.G(self.plus(b, k[7 * i + 4]), 13))
            e = self.G(self.plus(self.plus(b, c), k[7 * i + 3]), 21) ^ self.to_int_l(
                self.to_list(i + 1)
            )
            b = self.plus(b, e)
            c = self.minus(c, e)
            d = self.plus(d, self.G(self.plus(c, k[7 * i + 2]), 13))
            b = b ^ self.G(self.plus(a, k[7 * i + 1]), 21)
            c = c ^ self.G(self.plus(d, k[7 * i]), 5)
            a, b = b, a
            c, d = d, c
            a, d = d, a
        _a = self.to_list(a)
        _b = self.to_list(b)
        _c = self.to_list(c)
        _d = self.to_list(d)
        return _c + _a + _d + _b

    def rev(self, x):
        return self.to_int(self.to_list_l(x))


def solve(key, text):
    key = list(
        binascii.unhexlify("E9DEE72C8F0C0FA62DDB49F46F73964706075316ED247A3739CBA38303A98BF6")
    )
    text = list(binascii.unhexlify("B194BAC80A08F53B366D008E584A5DE4"))

    en = stb().encode(text, key)
    de = stb().decode(en, key)

    replace(key, text)

def replace(key, text):
    key = list(
        binascii.unhexlify("E9DEE72C8F0C0FA62DDB49F46F73964706075316ED247A3739CBA38303A98BF6")
    )
    text = list(
        binascii.unhexlify("B194BAC80A08F53B366D008E584A5DE48504FA9D1BB6C7AC252E72C202FDCE0D5BE3D61217B96181FE6786AD716B890B")
    )

    if len(text) < 16:
        raise Exception

    blocks = [text[i : i + 16] for i in range(0, len(text), 16)]
    r = [0 for _ in range(16 - len(blocks[-1]))]
    blocks[-1].extend(r)
    en_blocks = []
    for block in blocks:
        en_blocks.append(stb().encode(block, key))

    res = list(chain(*en_blocks))


    de_blocks = [stb().decode(block, key) for block in en_blocks]
    de_res = list(chain(*de_blocks))
    de_fin_res = [chr(item) for item in de_res]

    print([format(item, 'x') for item in res])
    chiper(key, text)

def chiper(key, text):
    def xor_mes(c, b):
        return [c[i] ^ b[i] for i in range(len(b))]

    key1 = list(
        binascii.unhexlify("E9DEE72C8F0C0FA62DDB49F46F73964706075316ED247A3739CBA38303A98BF6")
    )
    text1 = list(
        binascii.unhexlify("B194BAC80A08F53B366D008E584A5DE48504FA9D1BB6C7AC252E72C202FDCE0D5BE3D61217B96181FE6786AD716B890B")
    )

    s0 = list(binascii.unhexlify("BE32971343FC9A48A02A885F194B09A1"))

    s = s0

    if len(text1) < 16:
        raise Exception

    blocks = [text1[i : i + 16] for i in range(0, len(text1), 16)]
    r = [0 for _ in range(16 - len(blocks[-1]))]
    blocks[-1].extend(r)
    en_blocks = []

    for block in blocks:
        n_block = xor_mes(s, block)
        en_block = stb().encode(n_block, key1)
        en_blocks.append(en_block)
        s = en_block

    res = list(chain(*en_blocks))

    de_blocks = []
    s = s0
    for block in en_blocks:
        de_block = stb().decode(block, key1)
        de_blocks.append(xor_mes(s, de_block))
        s = block

    de_res = list(chain(*de_blocks))

    de_fin_res = [chr(item) for item in de_res]
from math import *
from core import *
import sys

functions = {
    '¡': lambda: 0,
    '¢': lambda: 0,
    '£': lambda: 0,
    '¤': lambda: 0,
    '¥': lambda: 0,
    '¦': lambda: 0,
    '©': lambda x: setRegister(x),
    '¬': lambda x: not x,
    '®': lambda: getRegister(),
    'µ': lambda: 0,
    '½': lambda x: sqrt(x),
    'Æ½': lambda x: int(sqrt(x)),
    'Ç': lambda: 0,
    'Ð': lambda: 0,
    'Ñ': lambda: 0,
    '×': lambda x, y: y * x,
    'Ø': lambda: 0,
    'ç': lambda: 0,
    'ð': lambda: 0,
    'ı': lambda x, y: y + x * 1j,
    'ȷ': lambda x, y: y * 10 ** x,
    'ñ': lambda: 0,
    '÷': lambda x, y: y // x if y % x == 0 and type(x) == type(0) and type(y) == type(0) else y / x,
    'ø': lambda: 0,
    ' ': lambda: 0,
    '!': lambda x: Pi(x),
    '"': lambda x: splat([x, x]),
    '#': lambda x: float(x) if '.' in x else int(x),
    '$': lambda: 0,
    '%': lambda: 0,
    '&': lambda x, y: True if y and x else False,
    '\'': lambda: 0,
    '*': lambda x, y: y ** x,
    '+': lambda x, y: y + x,
    ',': lambda: 0,
    '-': lambda x: -x,
    '.': lambda: 0,
    ':': lambda x, y: y // x,
    ';': lambda: 0,
    '<': lambda: 0,
    '=': lambda x, y: x == y,
    '>': lambda: 0,
    '?': lambda x, y, z: z if x else y,
    '@': lambda x: setRegisterNoReturn(x),
    'A': lambda x: abs(x),
    'B': lambda x: basedigits(x, 2),
    'C': lambda: 0,
    'D': lambda x: basedigits(x, 10),
    'E': lambda: 0,
    'F': lambda: 0,
    'G': lambda: 0,
    'H': lambda: 0,
    'I': lambda: 0,
    'J': lambda x: list(range(1, 1 + len(x if hasattr(x, '__getitem__') else str(x)))),
    'K': lambda: 0,
    'L': lambda x: len(x if hasattr(x, '__getitem__') else str(x)),
    'M': lambda: 0,
    'N': lambda: 0,
    'O': lambda x: (list(map(ord, x)) if len(x) > 1 else ord(x)) if hasattr(x, '__getitem__') else chr(int(x)),
    'P': lambda: 0,
    'Q': lambda: 0,
    'R': lambda x: list(range(1, 1 + x)),
    'S': lambda *a: sum(a),
    'T': lambda: 0,
    'U': lambda *a: splat(a[::-1]),
    'V': lambda: 0,
    'W': lambda: 0,
    'X': lambda: 0,
    'Y': lambda: 0,
    'Z': lambda: 0,
    '\\': lambda: 0,
    '^': lambda x, y: y ^ x,
    '_': lambda x, y: y - x,
    '`': lambda: 0,
    'a': lambda: 0,
    'b': lambda: 0,
    'c': lambda: 0,
    'd': lambda: 0,
    'e': lambda: 0,
    'f': lambda: 0,
    'g': lambda: 0,
    'h': lambda: 0,
    'i': lambda: 0,
    'j': lambda: 0,
    'k': lambda: 0,
    'l': lambda: 0,
    'm': lambda: 0,
    'n': lambda: 0,
    'o': lambda: 0,
    'p': lambda: 0,
    'q': lambda: 0,
    'r': lambda: 0,
    's': lambda: 0,
    't': lambda: 0,
    'u': lambda: 0,
    'v': lambda: 0,
    'w': lambda: 0,
    'x': lambda x, y: repeat(y, x),
    'y': lambda: 0,
    'z': lambda: 0,
    '|': lambda x, y: True if y or x else False,
    '~': lambda: 0,
    '¶': lambda: 0,
    '°': lambda: 0,
    '¹': lambda x: x,
    '²': lambda x: x ** 2,
    '³': lambda: 16,
    '⁴': lambda: 10,
    '⁵': lambda: 100,
    '⁶': lambda: 1000,
    '⁷': lambda: '',
    '⁸': lambda: '\n',
    '⁹': lambda: [],
    '⁺': lambda *a: splat(recursiveFilter(lambda x: x > 0, a, True)),
    '⁻': lambda *a: splat(recursiveFilter(lambda x: (type(x) == type(0) or type(x) == type(0.5)) and x < 0, a, False)),
    '⁼': lambda x, y: type(x) == type(y),
    '⁽': lambda: 0,
    '⁾': lambda: 0,
    'Ɓ': lambda: 0,
    'Ƈ': lambda: 0,
    'Ɗ': lambda: 0,
    'Ƒ': lambda: 0,
    'Ɠ': lambda: eval(input()),
    'Ƙ': lambda: 0,
    'Ɱ': lambda: 0,
    'Ɲ': lambda: 0,
    'Ƥ': lambda x: print(x),
    'Ƭ': lambda: 0,
    'Ʋ': lambda: 0,
    'Ȥ': lambda: 0,
    'ɓ': lambda: 0,
    'ƈ': lambda: sys.stdin.read(1),
    'ɗ': lambda: 0,
    'ƒ': lambda: 0,
    'ɠ': lambda: input(),
    'ɦ': lambda: 0,
    'ƙ': lambda: 0,
    'ɱ': lambda: 0,
    'ɲ': lambda: 0,
    'ƥ': lambda x: print(x, end = ''),
    'ɼ': lambda: 0,
    'ʂ': lambda: 0,
    'ƭ': lambda: 0,
    'ʋ': lambda: 0,
    'ȥ': lambda: 0,
    'Ạ': lambda x, y: y and x,
    'Ḅ': lambda: 0,
    'Ḍ': lambda: 0,
    'Ẹ': lambda: 0,
    'Ḥ': lambda: 0,
    'Ị': lambda: 0,
    'Ḳ': lambda: 0,
    'Ḷ': lambda x: list(range(x)),
    'Ṃ': lambda: 0,
    'Ṇ': lambda: 0,
    'Ọ': lambda x, y: y or x,
    'Ṛ': lambda: 0,
    'Ṣ': lambda: 0,
    'Ṭ': lambda: 0,
    'Ụ': lambda: 0,
    'Ṿ': lambda: 0,
    'Ẉ': lambda: 0,
    'Ỵ': lambda: 0,
    'Ẓ': lambda: 0,
    'Ȧ': lambda: 0,
    'Ḃ': lambda x: unbase(x, 2),
    'Ċ': lambda: 0,
    'Ḋ': lambda x: unbase(x, 10),
    'Ė': lambda: 0,
    'Ḟ': lambda: 0,
    'Ġ': lambda: 0,
    'Ḣ': lambda: 0,
    'İ': lambda: 0,
    'Ŀ': lambda x, y: levenshtein(castIterable(x), castIterable(y)),
    'Ṁ': lambda: 0,
    'Ṅ': lambda: 0,
    'Ȯ': lambda: 0,
    'Ṗ': lambda: 0,
    'Ṙ': lambda: 0,
    'Ṡ': lambda: 0,
    'Ṫ': lambda: 0,
    'Ẇ': lambda: 0,
    'Ẋ': lambda: 0,
    'Ẏ': lambda: 0,
    'Ż': lambda: 0,
    'ạ': lambda: 0,
    'ḅ': lambda: 0,
    'ḍ': lambda: 0,
    'ẹ': lambda: 0,
    'ḥ': lambda: 0,
    'ị': lambda: 0,
    'ḳ': lambda: 0,
    'ḷ': lambda: 0,
    'ṃ': lambda: 0,
    'ṇ': lambda: 0,
    'ọ': lambda: 0,
    'ṛ': lambda: 0,
    'ṣ': lambda: 0,
    'ṭ': lambda: 0,
    'ụ': lambda: 0,
    'ṿ': lambda: 0,
    'ẉ': lambda: 0,
    'ỵ': lambda: 0,
    'ẓ': lambda: 0,
    'ȧ': lambda: 0,
    'ḃ': lambda: 0,
    'ċ': lambda: 0,
    'ḋ': lambda: 0,
    'ė': lambda: 0,
    'ḟ': lambda: 0,
    'ġ': lambda: 0,
    'ḣ': lambda: 0,
    'ŀ': lambda: 0,
    'ṁ': lambda: 0,
    'ṅ': lambda: 0,
    'ȯ': lambda: 0,
    'ṗ': lambda: 0,
    'ṙ': lambda: 0,
    'ṡ': lambda: 0,
    'ṫ': lambda: 0,
    'ẇ': lambda: 0,
    'ẋ': lambda: 0,
    'ẏ': lambda: 0,
    'ż': lambda: 0,
    '«': lambda: 0,
    '»': lambda: 0,
    '‘': lambda x: x + 1,
    '’': lambda x: x - 1,
}

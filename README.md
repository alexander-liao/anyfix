# programming-language

Currently just a tokenizer test. Run `lang.py` and give it a program as input, and it will tokenize it.

# syntax

`“string”`: string of arbitrary length. `\k` for any character `k` currently returns `k` for most `k`; changes will be made later.  
`“string1“string2“string3”`: list of strings of arbitrary length, of arbitrary length. String syntax still applies  
`”c`: string of length `1`. `'\k` still works, still giving `k` though.  
`123`: number  
`0123`: octal  
`0b11`: binary  
`0q11`: quaternary  
`0x11`: hexadecimal
`[1 2 3]`: list. Can be nested like `[1 2 3 [4 5 6]]`. Try `[1[2[3[4]5]6]7]` :D  
`ßcode»`: sort over a key function. If top-of-stack is a list, sort that; otherwise, sort the whole stack  
`£code»`: map over a key function. If top-of-stack is a list, map that; otherwise, map the whole stack  
`þcode»`: filter over a key function. If top-of-stack is a list, filter that; otherwise, filter the whole stack  
`ʠcode»`: filter out over a key function. If top-of-stack is a list, filter out that; otherwise, apply on the whole stack  

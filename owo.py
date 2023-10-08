"""
Introducing you to the OwOpy module!
This module suits your OwOify needs perfectly, and it's customizable as well!
rams and applications.
It has 1 function - owoify()
The module's github link - https://github.com/Nimboss2411/OwOpy
"""
"""
MIT License

Copyright (c) 2021 Nimboss2411

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


# Modules
from random import choice

# Global variable initialisation
owo_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
owo_emotes = [
    "^w^",
    ">w< ",
    "UwU ",
    "(・`ω\\´・)",
    "(´・ω・\\`)",
    "OwO",
    "◔w◔ ",
    "( ͡o ω ͡o )",
    "(O꒳O)",
    "( °ω° )",
    "( ͡o ꒳ ͡o )",
    "ღ(O꒳Oღ)",
    "*𝓷𝓾𝔃𝔃𝓵𝓮𝓼 𝔂𝓸𝓾𝓻 𝓬𝓱𝓮𝓼𝓽*",
    "‿︵*𝓇𝒶𝓌𝓇*‿︵ ʘwʘ",
    "✼ ҉♡ (。O⁄ ⁄ω⁄ ⁄ O。) ҉♡ ✼",
    "✧･ﾟ: *✧･ﾟ:*(OwO)*:･ﾟ✧*:･ﾟ✧",
    "ᎧᏇᎧ",
    "♡w♡",
    "ÒwÓ",
    "≧◡≦",
    "✧(˘•ω•˘)ง",
    "~(˶‾᷄ꈊ‾᷅˵)~",
    "ᕙ(⇀w↼‶)ᕗ",
    "༼ ༎ຶ w ༎ຶ༽",
    "( ͡° w ͡°)",
    "(•w•)",
    "♤w♤",
    "♧w♧",
    "(๑و•̀ω•́)و",
    "(˶‾᷄ ⁻̫ ‾᷅˵)",
    "꒰๑´•.̫ • `๑꒱",
    "・ω・",
    ">ω^",
    "{・ω-*}",
    "ˁ(⦿@ᴥ⦿*)ˀ",
    "ʕ✿๑•́ ᴥ •̀๑✿ʔ",
    "(•̯͡.•̯͡)",
    "꒰◍ᐡᐤᐡ◍꒱",
    "༼ (´・ω・`) ༽",
    "♥(⇀ᆽ↼ﾐ)∫",
    "✿(≗ﻌ≗^)",
    "( ͒ ඉ .̫ ඉ ͒)",
    "( ^◡^)",
    "^•ﻌ•^",
    "{ @❛ꈊ❛@ }",
    "^•ﻌ•^ฅ",
    "(✿^U^)/",
    "(≗ﻌ≗^)",
]
__version__ = "0.0.2"


def owoify(owo_string: str, level: int = 3):
    """
    OwOifies (and UwUifies) your text!\n
    Usage - owopy.owoify('string', level) #level defaults to 2\n
    How levels work -\n
    There are three levels - 1, 2 and 3.\n
    The higher the level the more OwOified your text will be, try it out!
    """

    if not isinstance(owo_string, str):
        raise ValueError("n...nani?! the sentence awgument must be a stwing!")
    if not isinstance(level, int):
        raise ValueError("b...baka?! the level awgument must be a non-decimal numbew!")
    if not level in [1, 2, 3]:
        raise ValueError(
            "o...owo?! the level awgument must be between 1 and thwee (1 and 3 incwuded!)"
        )

    owo_string = (
        owo_string.replace("r", "w")
        .replace("R", "W")
        .replace("l", "w")
        .replace("L", "W")
        .replace("b", "bw")
        .replace("B", "BW")
    )

    if level == 3:
        owo_string = (
            owo_string.replace("o", "owo")
            .replace("O", "OwO")
            .replace("!", f"! {choice(owo_emotes)}{choice(owo_emotes)}")
            .replace("?", f"? {choice(owo_emotes)}{choice(owo_emotes)}")
            .replace(".", f"{choice(owo_emotes)}{choice(owo_emotes)}")
        )
    elif level == 2:
        owo_string = (
            owo_string.replace("!", f"! {choice(owo_emotes)}")
            .replace("?", f"? {choice(owo_emotes)}")
            .replace(".", f"{choice(owo_emotes)}")
        )

    for vowel in owo_vowels:
        if f"n{vowel}" in owo_string:
            owo_string = owo_string.replace(f"n{vowel}", f"ny{vowel}")
        elif f"N{vowel}" in owo_string:
            owo_string = owo_string.replace(f"N{vowel}", f"NY{vowel}")

    for vowel in owo_vowels:
        if f"b{vowel}" in owo_string:
            owo_string = owo_string.replace(f"b{vowel}", f"bw{vowel}")
        elif f"B{vowel}" in owo_string:
            owo_string = owo_string.replace(f"B{vowel}", f"BW{vowel}")

    if level == 2:
        owo_string = f"{choice(owo_emotes)} {owo_string} {choice(owo_emotes)}"
    elif level == 3:
        owo_string = f"{choice(owo_emotes)} {choice(owo_emotes)} {owo_string} {choice(owo_emotes)} {choice(owo_emotes)}"

    return owo_string

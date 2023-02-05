import re

from valid_password.core.regex import (
    length,
    uppercase,
    lowercase,
    digits,
    special_chars,
    repeated_chars,
)


def is_valid_rule(secret: str, size: int, rule: str) -> bool:
    rules_dict = {
        "minSize": length,
        "minUppercase": uppercase,
        "minLowercase": lowercase,
        "minDigit": digits,
        "minSpecialChars": special_chars,
        "noRepeted": repeated_chars,
    }
    if rule == "minSize":
        exp = re.compile(length.format(size=size))
        match = re.findall(exp, secret)
        result = True if match else False
    else:
        exp = re.compile(rules_dict.get(rule))
        match = re.findall(exp, secret)
        result = True if len(match) >= size else False

    return result

from typing import List, Tuple

from config import MAX_KEY_LENGTH, MIN_KEY_LENGTH, SPECIAL_CHARS


def validate_key(key: str) -> Tuple[bool, List[str]]:
    is_valid, failures = _validate_key_recursive(
        key, 0, False, False, False, False, 1, 0
    )
    return is_valid, failures


def _validate_key_recursive(
    key: str,
    index: int,
    has_upper: bool,
    has_lower: bool,
    has_digit: bool,
    has_special: bool,
    consecutive: int,
    max_consecutive: int,
) -> Tuple[bool, List[str]]:
    if index == len(key):
        failures = []
        if len(key) < MIN_KEY_LENGTH or len(key) > MAX_KEY_LENGTH:
            failures.append("key_length")
        if not has_upper:
            failures.append("key_uppercase")
        if not has_lower:
            failures.append("key_lowercase")
        if not has_digit:
            failures.append("key_digit")
        if not has_special:
            failures.append("key_special")
        if max_consecutive > 3:
            failures.append("key_consecutive")
        return len(failures) == 0, failures

    char = key[index]

    new_upper = has_upper or char.isupper()
    new_lower = has_lower or char.islower()
    new_digit = has_digit or char.isdigit()
    new_special = has_special or char in SPECIAL_CHARS

    if index > 0 and char == key[index - 1]:
        new_consecutive = consecutive + 1
    else:
        new_consecutive = 1

    new_max_consecutive = max(max_consecutive, new_consecutive)

    return _validate_key_recursive(
        key,
        index + 1,
        new_upper,
        new_lower,
        new_digit,
        new_special,
        new_consecutive,
        new_max_consecutive,
    )

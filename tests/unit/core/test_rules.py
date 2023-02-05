import pytest

from valid_password.core.rules import is_valid_rule


def test_validate_min_size_rule():
    assert is_valid_rule("secret", 6, "minSize") is True


def test_validate_min_size_rule_invalid():
    assert is_valid_rule("secret", 8, "minSize") is False


def test_validate_min_uppercase_rule():
    assert is_valid_rule("Secret", 1, "minUppercase") is True


def test_validate_min_uppercase_invalid():
    assert is_valid_rule("secret", 8, "minUppercase") is False


def test_validate_min_lowercase_rule():
    assert is_valid_rule("secret", 1, "minLowercase") is True


def test_validate_min_lowercase_invalid():
    assert is_valid_rule("SEcret", 5, "minLowercase") is False


def test_validate_min_digit_rule():
    assert is_valid_rule("s3cr3t", 2, "minDigit") is True


def test_validate_min_digit_invalid():
    assert is_valid_rule("SEcret", 5, "minDigit") is False


def test_validate_min_special_chars_rule():
    assert is_valid_rule("secret!@", 2, "minSpecialChars") is True


def test_validate_min_special_chars_invalid():
    assert is_valid_rule("SEcret", 3, "minSpecialChars") is False


def test_validate_no_repeated_chars_rule():
    assert is_valid_rule("secret!@", 0, "noRepeted") is True


def test_validate_no_repeated_chars_rule_invalid():
    assert is_valid_rule("ssecret", 0, "noRepeted") is True

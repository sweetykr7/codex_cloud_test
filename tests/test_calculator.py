import pytest

from calculator import evaluate


def test_basic_math():
    assert evaluate("1 + 2 * 3") == 7.0


def test_parentheses():
    assert evaluate("(1 + 2) * 3") == 9.0


def test_division_by_zero():
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
        evaluate("1 / 0")


def test_invalid_characters():
    with pytest.raises(ValueError, match="허용되지 않은 문자가 포함"):
        evaluate("__import__('os').system('echo bad')")

"""간단한 사칙연산 계산기.

사용 예시:
    python calculator.py "1 + 2 * 3"
"""

from __future__ import annotations

import argparse


ALLOWED_CHARS = set("0123456789+-*/(). ")


def evaluate(expression: str) -> float:
    """주어진 수식을 계산해서 결과를 반환한다."""
    if not expression or not expression.strip():
        raise ValueError("빈 수식은 계산할 수 없습니다.")

    if any(ch not in ALLOWED_CHARS for ch in expression):
        raise ValueError("허용되지 않은 문자가 포함되어 있습니다.")

    try:
        result = eval(expression, {"__builtins__": {}}, {})
    except ZeroDivisionError as exc:
        raise ValueError("0으로 나눌 수 없습니다.") from exc
    except Exception as exc:
        raise ValueError("올바른 수식을 입력해주세요.") from exc

    if not isinstance(result, (int, float)):
        raise ValueError("숫자 계산만 허용됩니다.")

    return float(result)


def main() -> None:
    parser = argparse.ArgumentParser(description="파이썬 계산기")
    parser.add_argument("expression", help='계산할 수식 (예: "1 + 2 * 3")')
    args = parser.parse_args()

    print(evaluate(args.expression))


if __name__ == "__main__":
    main()

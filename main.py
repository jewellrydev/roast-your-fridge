#!/usr/bin/env python3
"""Cold Shoulder — entry for One Line, One Laugh: Roast Your Fridge on make.fun.

Prints exactly one line (at most 200 characters) roasting a fridge.
"""

LINE = "My fridge runs all day, produces nothing but cold air and judgment, and still hums all night like it is doing something important."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()

from typing import Annotated


def process_value(
        value: Annotated[int, "範囲: 0 <= vlue <= 100"]
) -> None:
    if 0 <= value <= 100:
        print(f"受け取った値は範囲内です: {value}")
    else:
        raise ValueError(f"範囲外の値です。受けたった値: {value}")


process_value(50)


try:
    process_value(0)
except ValueError as e:
    print(e)

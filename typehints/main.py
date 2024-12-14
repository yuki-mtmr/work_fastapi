from typing import Dict
from typing import List


def add(num1: int, num2: int) -> str:
    result: str = '足し算結果=>'
    return result + str(num1 + num2)


def greet(name: str) -> str:
    return f"おはよう！{name}!"


def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor


def get_first_three_elements(elements: List[int]) -> List[int]:
    return elements[:3]


def get_value(dictionary: Dict[str, int], key: str) -> int:
    return dictionary[key]


def process_items(items: list[str]) -> None:
    for item in items:
        print(item)


def count_characters(word_list: list[str]) -> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        count_map[word] = len(word)
    return count_map


result_add = add(10, 20)
print(result_add)

greeting = greet("タロウ")
print(greeting)

result_divide = divide(10.0, 2.0)
print("割り算の結果=>", result_divide)

elements = get_first_three_elements([1, 2, 3, 4, 5])
print("最初から値を3個取り出す=>", elements)

value = get_value({'a': 1, 'b': 2, 'c': 3}, 'b')
print("キーワード「b」に対する値は=>", value)

process_items(["リンゴ", "ゴリラ", "ラッパ"])

character_counts = count_characters(["apple", "amazon", "google"])
print("文字に対する文字数は=>", character_counts)

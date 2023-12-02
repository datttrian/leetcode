## Arrays & Hashing

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        value_to_symbol = dict(zip(values, symbols))

        result = ""

        for value in values:
            while num >= value:
                num -= value
                result += value_to_symbol[value]

        return result


```

The time complexity of this solution is O(1) because the number of iterations in the for loop is constant. The space complexity is also O(1) because the size of the input does not affect the amount of space used.

## Two Pointers

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        result = ""
        i = 0
        j = 0

        while num > 0:
            count, num = divmod(num, values[i])
            result += symbols[j] * count

            i += 1
            j += 1

        return result


```

The time complexity of this solution is O(1) because the while loop will iterate a constant number of times, regardless of the input value of num. The space complexity is also O(1) because the size of the input does not affect the amount of memory used by the algorithm.

## Stack

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        result = []

        for value, symbol in zip(values, symbols):
            while num >= value:
                num -= value
                result.append(symbol)

        return "".join(result)


```

The time complexity of this solution is O(1) because the number of iterations in the for loop is constant, regardless of the value of the input num. The space complexity is also O(1) because the size of the result list does not depend on the input size.

## Greedy

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result


```

## Math & Geometry

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_extend_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        result = ""

        for value, symbol in roman_extend_dict.items():
            count, num = divmod(num, value)

            result += symbol * count

        return result

```

The time complexity of this solution is O(1) because the input number is limited to a range of 1 to 3999, which means the loop will iterate a maximum of 13 times. Therefore, the time complexity is constant.

The space complexity is also O(1) because the space used by the solution does not depend on the input size. The dictionary and the result string have a fixed size and do not grow with the input.
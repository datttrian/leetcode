class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove leading and trailing whitespaces

        def is_integer(s: str) -> bool:
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def is_decimal(s: str) -> bool:
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, _, fractional_part = s.partition('.')
            return (
                integer_part.isdigit() or not integer_part
            ) and fractional_part.isdigit()

        def is_scientific_notation(s: str) -> bool:
            if 'e' not in s and 'E' not in s:
                return False
            base, _, exponent = (
                s.partition('e') if 'e' in s else s.partition('E')
            )
            return (is_integer(base) or is_decimal(base)) and is_integer(
                exponent,
            )

        if '.' in s:
            return is_decimal(s)
        elif 'e' in s or 'E' in s:
            return is_scientific_notation(s)
        else:
            return is_integer(s)

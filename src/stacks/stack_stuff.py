from typing import List


class StackStuff:

    def reverse_list_via_stack(self, input_list: List[int]) -> List[int]:
        stack = []
        output = []
        for i in input_list:
            stack.append(i)
        while stack:
            output.append(stack.pop())
        return output

    def is_valid_parenthesis(self, input_str: str) -> bool:
        stack = []
        open_char = {"(": ")", "{": "}", "[": "]"}
        for c in input_str:
            if c in open_char:
                stack.append(c)
            else:
                if len(stack) > 0 and c == open_char.get(stack[-1]):
                    stack.pop()
                else:
                    return False
        return not stack

    def find_first_bigger_right(self, input_arr: List[int]) -> List[int]:
        stack = [(input_arr[0], 0)]
        output = [-1] * len(input_arr)
        for i in range(1, len(input_arr)):
            largest = input_arr[i]
            while stack and largest > stack[-1][0]:
                output[stack[-1][1]] = largest
                stack.pop()
            stack.append((largest, i))
        return output

    def handle_equation(self, input_equation):
        ...

    def tokenize_input_str(self, input_equation: str) -> int:
        previous_val_queue = [(1, 0)]
        total = 0
        current_num = 0
        current_sign = 1
        for c in input_equation:
            if c in {"+", "-"}:
                total += (current_num * current_sign)
                current_sign = -1 if c == "-" else 1
                current_num = 0
            if c.isdigit():
                current_num = (current_num * 10) + int(c)
            if c == "(":
                previous_val_queue.append((current_sign, total))
                total = 0
                current_sign = 1
            if c == ")":
                total += (current_num * current_sign)
                last = previous_val_queue[-1]
                total *= last[0]
                total += last[1]
                current_num = 0
            print(f"c: {c}, total: {total}, n: {current_num}, s: {current_sign}, q: {previous_val_queue}")
        return total + current_num * current_sign

    def perform_math(self, input_equation: str) -> int:
        previous_val_queue = [(1, 0)]
        total = 0
        current_num = 0
        current_sign = 1
        for c in input_equation:
            if c in {"+", "-"}:
                total += (current_num * current_sign)
                current_sign = -1 if c == "-" else 1
                current_num = 0
            if c.isdigit():
                current_num = (current_num * 10) + int(c)
            if c == "(":
                previous_val_queue.append((current_sign, total))
                total = 0
                current_sign = 1
            if c == ")":
                total += (current_num * current_sign)
                last = previous_val_queue[-1]
                total *= last[0]
                total += last[1]
                current_num = 0
            print(f"c: {c}, total: {total}, n: {current_num}, s: {current_sign}, q: {previous_val_queue}")
        return total + current_num * current_sign


    def __is_char_digit__(self, c: str):
        if 1 < len(c) or len(c) <= 0:
            return False
        return ord('0') <= (ord(c)) <= ord('9')

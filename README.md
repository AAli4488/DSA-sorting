# Valid Parentheses (LeetCode #20)

**Difficulty:** Easy
**Topics:** String, Stack
**Link:** https://leetcode.com/problems/valid-parentheses/

## Problem

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

A string is valid if:

1. Open brackets are closed by the same type of bracket.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the same type.

## Examples

| Input      | Output  | Reason                                  |
|------------|---------|-----------------------------------------|
| `"()[]{}"` | `True`  | Every bracket is closed by its match    |
| `"(]"`     | `False` | Wrong type of closing bracket           |
| `"([)]"`   | `False` | Brackets are closed in the wrong order  |
| `"{[]}"`   | `True`  | Properly nested                         |
| `"(("`     | `False` | Opening brackets are never closed       |

## Approach

Use a **stack**:

1. Go through the string one character at a time.
2. If the character is an opening bracket, push it onto the stack.
3. If it is a closing bracket, the top of the stack must be its matching opener. If the stack is empty or the top doesn't match, return `False`.
4. After the loop, the string is valid only if the stack is empty (no unclosed brackets remain).

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:  # opening bracket
                stack.append(ch)

        return not stack  # valid only if nothing is left open
```

## Complexity

- **Time:** O(n), since each character is processed once.
- **Space:** O(n), since the stack can hold up to n characters in the worst case.

## Running Locally

```python
sol = Solution()
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))      # False
print(sol.isValid("([)]"))    # False
print(sol.isValid("{[]}"))    # True
print(sol.isValid("(("))      # False

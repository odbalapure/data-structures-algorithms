def is_valid(string: str) -> bool:
    """
    :Time: O(N^2)
    :Space: O(N)
    """
    while "()" in string or "{}" in string or "[]" in string:
        string = string.replace("()", "")
        string = string.replace("{}", "")
        string = string.replace("[]", "")
    return string == ""


def is_valid(string: str) -> bool:
    """
    :Time: O(N)
    :Space: O(N)
    """
    stack = []
    close_to_open = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            print(char)
            stack.append(char)

    return not stack


print(is_valid("([])"))

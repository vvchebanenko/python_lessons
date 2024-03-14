price: int = 5
title: str

def indent_right(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print("dir(indent_right)")
print(dir(indent_right))

print()

print("indent_right.__annotations__")
print(indent_right.__annotations__)

print("type(indent_right)")
print(type(indent_right))

# print(isinstance(indent_right, function))         ?
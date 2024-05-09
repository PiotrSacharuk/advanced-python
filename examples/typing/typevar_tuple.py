from typing_extensions import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')

def concat(*args: Unpack[Ts]) -> Tuple[Unpack[Ts]]:
    return args

# Usage of concat
result = concat(1, "hello", 3.14)
print(result)  # Output: (1, 'hello', 3.14)
# 限制参数值范围
def value_range(
    val: float,
    min: float = float("-inf"),
    max: float = float("-inf"),
):
    if val < min:
        val = min
    elif val > max:
        val = max
    return val

def Handle_point(value: tuple):
    result = {"id": value[0]}
    if len(value) ==2:
        result["name"] = value[1]
    return result
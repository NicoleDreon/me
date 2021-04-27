def cast_int(str):
    """Cast string to int if a value is given."""

    try:
        num = int(str)
        return num
    except(ValueError, TypeError):
        return None

def cast_float(str):
    """Cast string to float if a value is given."""

    try:
        num = float(str)
        return num
    except(ValueError, TypeError):
        return None
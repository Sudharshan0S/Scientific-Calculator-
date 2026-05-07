import math

ANGLE_MODE = "DEG"


def set_angle_mode(mode):

    global ANGLE_MODE

    ANGLE_MODE = mode


def sin_function(x):

    if ANGLE_MODE == "DEG":

        return math.sin(math.radians(x))

    return math.sin(x)


def cos_function(x):

    if ANGLE_MODE == "DEG":

        return math.cos(math.radians(x))

    return math.cos(x)


def tan_function(x):

    if ANGLE_MODE == "DEG":

        return math.tan(math.radians(x))

    return math.tan(x)


allowed_names = {

    "sqrt": math.sqrt,

    "sin": sin_function,

    "cos": cos_function,

    "tan": tan_function,

    "log": math.log10,

    "ln": math.log,

    "factorial": math.factorial,

    "pi": math.pi,

    "e": math.e,
}


def safe_calculate(expression):

    return eval(
        expression,
        {"__builtins__": None},
        allowed_names
    )
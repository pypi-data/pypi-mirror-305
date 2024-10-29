from calculator_bundle.adder import add
from calculator_bundle.multiplier import multiply

def calculate(a: float, b: float) -> dict:
    return {
        "addition": add(a, b),
        "multiplication": multiply(a, b)
    }

from src.calculator.security.safe_eval import safe_calculate

class ExpressionParser:
    @staticmethod
    def evaluate(expression):
        return safe_calculate(expression)

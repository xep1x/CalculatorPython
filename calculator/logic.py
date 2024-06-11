# calculator/logic.py

def evaluate_expression(expression):
    try:
        # Оценка выражения с использованием eval, но в реальном приложении стоит использовать более безопасный метод
        result = eval(expression)
    except Exception as e:
        result = "Error"
    return result

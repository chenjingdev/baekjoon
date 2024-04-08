import re
# expression = "2-4-10+12+2-2"
expression = input()
pattern = r"(\d+(?:\+\d+)+)"
def remove_leading_zeros(expression):
    return re.sub(r'\b0+(\d+)', r'\1', expression)
modified_expression = remove_leading_zeros(re.sub(pattern, r"(\1)", expression))

# 수식 계산
def calculate_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return f"An error occurred: {e}"

# 결과 출력
result = calculate_expression(modified_expression)
print(result)
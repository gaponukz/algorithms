import string
import itertools

from expression import Expression

def print_bool_table(str_expression: str) -> None:
    variables = list(set([item[1] for item in string.Formatter().parse(str_expression) if item[1] is not None]))

    for bool_args in list(itertools.product(["0", "1"], repeat=len(variables))):
        formtaed_expression = str_expression.format(**{ variables[i]: bool_args[i] for i in range(len(variables)) })
        result = Expression(formtaed_expression).apply()
        variables_values = " ".join([f"{variables[i]} = {bool_args[i]}" for i in range(len(variables))])

        print(f"{variables_values} | {formtaed_expression} = {int(result)}")

if __name__ == "__main__":
    # print_bool_table("{x} and {y} or not ({z} and {y})")
    
    print_bool_table("({x} and ({x} impl {y})) impl {y}")

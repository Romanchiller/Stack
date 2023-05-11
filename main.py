from Classes import Stack
from tools import el_in_stack_end

balance1 = '(((([{}]))))'
balance2 = '[([])((([[[]]])))]{()}'
balance3 = '{{[()]}}'
not_balance1 = '}{}'
not_balance2 = '{{[(])]}}'
not_balance3 = '[[{())}]'



def balance(str_with_staples):
    if len(str_with_staples) % 2 == 1:
        return print('Несбаласировано')
    else:
        stack = Stack()
        for el in str_with_staples:
            if el == '[' or el == '(' or el == '{':
                stack.push(el)
            if el == ']':
                x = el_in_stack_end(stack, '[')
                if x is False:
                    return print('Несбаласировано')
            if el == ')':
                x = el_in_stack_end(stack, '(')
                if x is False:
                    return print('Несбаласировано')
            if el == '}':
                x = el_in_stack_end(stack, '{')
                if x is False:
                    return print('Несбаласировано')

        if stack.size() > 0:
            return print('Несбалансировано')
        else:
            return print('Сбалансировано')

if __name__ == '__main__':
    balance(balance1)
    balance(balance2)
    balance(balance3)
    balance(not_balance1)
    balance(not_balance2)
    balance(not_balance3)

def el_in_stack_end(any_stack, el):
    last_el = any_stack.peek()
    if last_el != el:
        return False
    else:
        return any_stack.pop()


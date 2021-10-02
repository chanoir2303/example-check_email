def check_email(string):
    space = ' ' in string
    dot = '.' in string
    at = '@' in string
    state = 0
    if string.endswith('.com'):
        if space:
            state = False
        elif at and dot:
            state = True
            x = string.index('@')
            y = string.index('.')
            if x < y:
                state = True
            if x + 1 == y:
                state = False
    return state

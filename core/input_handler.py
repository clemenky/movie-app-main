import sys

from globals import INPUT_SYMBOL


def get_user_selection(input_config):
    mode = input_config.get('mode')
    options = input_config.get('options', [])

    if mode == 'text':
        return get_text_input(options)
    elif mode == 'selection':
        return get_selection_input(options)

def get_text_input(options):
    option = options[0]
    param = option['param']
    validate = option.get('validate', lambda x: True)
    action = option.get('action', '')

    error_printed = False
    while True:
        user_input = input(INPUT_SYMBOL + ' ').strip().lower()

        if validate(user_input):
            return action, {param: user_input}
        
        print_input_error(error_printed)
        error_printed = True

def get_selection_input(options):
    valid_inputs = {opt.get('input'): opt for opt in options}

    error_printed = False
    while True:
        user_input = input(INPUT_SYMBOL + ' ').strip().lower()

        if user_input in valid_inputs:
            action = valid_inputs[user_input].get('action', '')
            return action, {}
        
        print_input_error(error_printed)
        error_printed = True

def print_input_error(error_printed):
    if error_printed:
        clear_previous_line()
    clear_previous_line()
    print("Invalid input. Please try again.")
    flush_console()

def clear_previous_line():
    move_console_cursor_up()
    clear_console_line()
    flush_console()

def clear_console_line():
    sys.stdout.write('\x1b[2K')
    sys.stdout.write('\r')

def move_console_cursor_up():
    sys.stdout.write(f'\x1b[1A')

def flush_console():
    sys.stdout.flush()
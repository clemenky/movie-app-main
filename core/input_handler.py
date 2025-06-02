import sys


INPUT_SYMBOL = '>'


def get_user_selection(input_config):
    mode = input_config.get('mode')
    options = input_config.get('options', [])

    if mode == 'text':
        return get_text_input(options)
    elif mode == 'selection':
        return get_selection_input(options)

def get_text_input(options):
    option = options[0]

    param_name = option['target_param']
    validate_input = option.get('validate', lambda x: True)
    screen_key, screen_params = option.get('target', ('', {}))

    error_shown = False

    while True:
        user_input = input(INPUT_SYMBOL + ' ').strip().lower()

        if validate_input(user_input):
            screen_params[param_name] = user_input
            return screen_key, screen_params
        
        print_input_error(error_shown)
        error_shown = True

def get_selection_input(options):
    input_map = {opt.get('input'): opt for opt in options}

    error_shown = False
    while True:
        user_input = input(INPUT_SYMBOL + ' ').strip().lower()

        if user_input in input_map:
            target = input_map[user_input].get('target', ('', {}))
            return target
        
        print_input_error(error_shown)
        error_shown = True

def print_input_error(error_shown):
    if error_shown:
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
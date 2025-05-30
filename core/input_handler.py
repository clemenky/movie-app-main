import sys

from globals import INPUT_SYMBOL


def get_user_selection(input_options, output_params):
    action = get_user_selected_action(input_options)
    return action

def get_user_selected_action(input_options):
    error_printed = False

    while True:
        user_input = input(INPUT_SYMBOL + ' ').strip().lower()

        if is_valid_option(user_input, input_options):
            return get_action_for_input(user_input, input_options)
        
        if error_printed:
            move_console_cursor_up(1)
            clear_console_line()
        
        move_console_cursor_up(1)
        clear_console_line()
        print("Invalid input. Please try again.")

        error_printed = True

def is_valid_option(user_input, input_options):
    for option in input_options:
        if user_input == option.get('input'):
            return True
    
    return False

def get_action_for_input(user_input, input_options):
    for option in input_options:
        if user_input == option.get('input'):
            return option.get('action', '')
    
    return ''


def clear_console_line():
    sys.stdout.write('\x1b[2K')
    sys.stdout.write('\r')

def move_console_cursor_up(lines=1):
    sys.stdout.write(f'\x1b[{lines}A')

def move_console_cursor_down(lines=1):
    sys.stdout.write(f'\x1b[{lines}B')

def flush_console():
    sys.stdout.flush()
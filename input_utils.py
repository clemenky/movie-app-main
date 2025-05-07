def display_options(options):
    for option in options:
        if not option.get('hidden', False):
            print(f"{option['input']}: {option['text']}")

input_symbol = '> '

def handle_input(params):
    options = params.get('options', [])
    text_input = params.get('text_input')
    title = params.get('title')
    prompt = params.get('prompt', '')
    input_error = params.get('input_error', 'Invalid input.\n')
    
    while True:
        if title:
            print(title)
        if prompt:
            print(prompt)
        if options:
            display_options(options)

        print('')
        user_input = input(input_symbol).strip().lower()
        print('')

        # Matched fixed options
        match = next((opt for opt in options if opt['input'] == user_input), None)
        if match:
            ###
            confirmation_message = match.get('confirmation')
            if confirmation_message:
                confirm = input(f'{confirmation_message} (y/n): ').strip().lower()
                if confirm != 'y':
                    continue
            ###
            return (
                match['function'],
                match.get('params', {})
            )
        
        # Fallback to text input handling
        if text_input:
            validator = text_input.get('validate', lambda x: True)
            if validator(user_input):
                return (
                    text_input['function'],
                    {text_input.get('param_name', 'input'): user_input}
                )
        
        print(input_error)

from wcwidth import wcswidth

from .utils import apply_spacing


OPTION_FORMATS = {
    'square_brackets': ('[', ']'),
    'none': ('', '')
}

MIN_DESCRIPTION_PADDING = 8

def render(component_props):
    output = ''
    style = component_props.get('style', {})

    prompt = component_props.get('prompt', None)
    if prompt is not None:
        output += prompt + '\n'
        spacing_after_prompt = style.get('spacing_after_prompt', 1)
        output += '\n' * spacing_after_prompt
    
    option_format = style.get('option_format', 'none')
    show_icons = style.get('icons', False)
    options = component_props.get('options', [])

    # Calculate max width of (input + icon + label) for description padding
    max_main_width = 0
    for option in options:
        main_text = build_main_text(option, option_format, show_icons)
        display_width = wcswidth(main_text)
        max_main_width = max(max_main_width, display_width)

    option_lines = []
    for option in options:
        option_line = build_option_line(option, option_format, show_icons, max_main_width)
        option_lines.append(option_line)
    
    output += '\n'.join(option_lines)
    output = apply_spacing(output, component_props)
    print(output)

def build_main_text(option_props, option_format='none', show_icon=False):
    option_input = option_props.get('input', '')
    label = option_props.get('label', '')
    icon = option_props.get('icon', '')

    input_prefix, input_suffix = OPTION_FORMATS.get(option_format, ('', ''))
    input_formatted = f'{input_prefix}{option_input}{input_suffix} '

    parts = [input_formatted]
    if show_icon:
        parts.append(f'{icon} ')
    parts.append(label)

    return ''.join(parts)

def build_option_line(option_props, option_format='none', show_icon=False, max_main_width=0):
    description = option_props.get('description', '')

    main_text = build_main_text(option_props, option_format, show_icon)
    main_text_width = wcswidth(main_text)
    padding_spaces = max(0, max_main_width - main_text_width)

    padding = ' ' * (padding_spaces + MIN_DESCRIPTION_PADDING)

    if description:
        description = '- ' + description

    parts = [main_text, padding, description]
    output_line = ''.join(parts)
    output_line = apply_spacing(output_line, option_props)
    return output_line
    

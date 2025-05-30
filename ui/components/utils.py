from wcwidth import wcswidth

from globals import DIVIDER_WIDTH


def apply_spacing(text, component_props):
    style = component_props.get('style', {})
    spacing_before = '\n' * style.get('spacing_before', 0)
    spacing_after = '\n' * style.get('spacing_after', 0)
    return f'{spacing_before}{text}{spacing_after}'

def center_text(text):
    text_width = wcswidth(text)
    if text_width >= DIVIDER_WIDTH:
        return text
    padding = (DIVIDER_WIDTH - text_width) // 2
    return ' ' * padding + text

def build_divider(char='='):
    return char * DIVIDER_WIDTH

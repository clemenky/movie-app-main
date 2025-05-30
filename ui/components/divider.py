from .utils import apply_spacing, build_divider


def render(component_props):
    default_char = '='
    char = component_props.get('char', default_char)

    if not char:
        char = default_char

    char = char[0]

    divider = build_divider(char)
    divider = apply_spacing(divider, component_props)
    print(divider)
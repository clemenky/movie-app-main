from .utils import apply_spacing, center_text, build_divider


def render(component_props):
    style = component_props.get('style', {})
    show_icons = style.get('icon', True)
    title_text = component_props['text']

    if style.get('uppercase', False):
        title_text = title_text.upper()

    if show_icons:
        icon = component_props['icon']
        title = f'{icon}  {title_text}  {icon}'
    else:
        title = f'{title_text}'

    title = center_text(title)
    divider = build_divider()

    output = f'{divider}\n{title}\n{divider}'
    output = apply_spacing(output, component_props)
    print(output)

from .utils import center_text, get_divider


def render(component_props):
    content = component_props['content']
    show_icons = content.get('icon', True)
    title_text = content['text']

    if show_icons:
        icon = content['icon']
        decorated_title = f'{icon}  {title_text}  {icon}'
    else:
        decorated_title = f'{title_text}'

    title_formatted = center_text(decorated_title)
    divider = get_divider()

    print(divider)
    print(title_formatted)
    print(divider)
    print()

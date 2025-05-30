from .utils import apply_spacing, center_text


def render(component_props):
    style = component_props.get('style', {})
    text = component_props.get('text', '')
    align_center = style.get('center', False)

    if align_center:
        text = center_text(text)
    
    text = apply_spacing(text, component_props)
    print(text)

from core.global_context import app_context


def render_screen(screen_props):
    for component_props in screen_props:
        component_type = component_props.get('component')
        renderer = app_context.screen_components.get_component(component_type)

        if not renderer:
            raise ValueError(f'Component type \'{component_type}\' unknown')
        
        renderer.render(component_props)

import ui.screen_renderer as screen_renderer
import core.input_handler as input_handler


def handle_screen(screen_module, screen_name):
    component_props = getattr(screen_module, screen_name).screen
    input_config = getattr(screen_module, screen_name).input_config

    screen_renderer.render_screen(component_props)
    return input_handler.get_user_selection(input_config)
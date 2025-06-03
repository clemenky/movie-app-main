import copy

import ui.screen_renderer as screen_renderer
import core.input_handler as input_handler


def handle_screen(screen_module, screen_name, dynamic_screen_components=None, dynamic_input_options=None):
    if dynamic_screen_components is None:
        dynamic_screen_components = {}
    if dynamic_input_options is None:
        dynamic_input_options = {}

    component_props = copy.deepcopy(getattr(screen_module, screen_name).screen_components)
    input_config = copy.deepcopy(getattr(screen_module, screen_name).input_config)

    component_props = inject_dynamic_content(component_props, dynamic_screen_components, 'screen_components')
    input_config['options'] = inject_dynamic_content(input_config['options'], dynamic_input_options, 'input_options')

    screen_renderer.render_screen(component_props)
    return input_handler.get_user_selection(input_config)

def inject_dynamic_content(base_list, placeholder_replacements, content_type):
    if content_type == 'screen_components':
        placeholder_key = 'component'
    elif content_type == 'input_options':
        placeholder_key = 'kind'
    else:
        return base_list

    new_list = []
    for item in base_list:
        if item.get(placeholder_key) == 'dynamic_placeholder':
            placeholder_id = item.get('id')
            content_to_insert = placeholder_replacements.get(placeholder_id)

            if content_to_insert:
                new_list.extend(content_to_insert)
                
        else:
            new_list.append(item)
    
    return new_list

import importlib
import os


class ScreenComponentsManager:
    def __init__(self):
        self.components_package = 'ui.components'
        self._components = {}
        self._excluded_files = {'__init__.py', 'utils.py'}
        self._load_components()

    def _load_components(self):
        package_path = self.components_package.replace('.', os.sep)
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(root_path, package_path)

        for filename in os.listdir(full_path):
            if filename.endswith('.py') and filename not in self._excluded_files:
                module_name = filename[:-3]
                full_module_name = f'{self.components_package}.{module_name}'
                module = importlib.import_module(full_module_name)
                self._components[module_name] = module

    def get_component(self, name):
        return self._components.get(name)
    
    def get_all_components(self):
        return self._components

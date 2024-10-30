import yaml
import random
import importlib.resources


class CollectionFinder:
    with importlib.resources.open_text("iriiifassemble.config", "config.yml") as file:
        config = yaml.safe_load(file)
    collections = config['collections']

    def get_random(self):
        return random.choice(self.collections)

    def get_by_id(self, identifier):
        return self.collections[identifier]

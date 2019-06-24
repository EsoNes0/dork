"""Returns yaml data as a dict"""
import yaml


__all__ = ["load"]


def load(file_name):
    """Loads yaml data from the given file_name"""

    file_path = f"./dork/yaml/{file_name}.yml"
    with open(file_path) as file:
        data = yaml.safe_load(file.read())
    return data
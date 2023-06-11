import yaml

def load_file(path):
    with open(path) as f:
        result = yaml.safe_load(f)        
    return result
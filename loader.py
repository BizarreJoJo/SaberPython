import yaml

def load_file(path):
    try:
        with open(path) as f:
            result = yaml.safe_load(f)        
        return result
    except FileNotFoundError:
        exit('No such file: ' + path)

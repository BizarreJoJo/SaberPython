import yaml

def save(path):
    
    with open('config.yaml', 'w') as f:
        yaml.safe_dump({'default_path': path}, f)
        return 'Default path has changed'
        
def load():
    
    with open('config.yaml') as f:
        return yaml.safe_load(f)

def reset():
    
    with open('config.yaml', 'w') as f:
        yaml.safe_dump({'default_path': ''}, f)
        return 'Default path has restored'
        
def get_path(path):
    path = str(path or load()['default_path'] or '')
    if path and not path[-1] in ('\\','/'):
        path += '\\'
    return path
import config
import loader

def get_list(path, message, filename, key):
    path = config.get_path(path)
    result = message + '\n{}'.format(
        '\n'.join([
            ' * ' + i['name']
            for i in loader.load_file(path + filename)[key]
            ])
        )
    return result